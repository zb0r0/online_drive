import os
import requests
from flask import render_template, url_for, redirect, flash, request, send_from_directory, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from backend.app import app, db, login_manager
from backend.models import User, FileStorage
from backend.forms import RegistrationForm, LoginForm, UploadFileForm
import logging

def get_payu_access_token():
    response = requests.post(
        f"{app.config['PAYU_API_URL']}/pl/standard/user/oauth/authorize",
        data={
            'grant_type': 'client_credentials',
            'client_id': app.config['PAYU_CLIENT_ID'],
            'client_secret': app.config['PAYU_CLIENT_SECRET']
        }
    )

    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        logging.error('Failed to obtain access token from PayU')
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home_page():
    if current_user.is_authenticated:
        files = FileStorage.query.filter_by(user_id=current_user.id).all()
        files_data = [{
            'id': file.id,
            'filename': file.filename,
            'filepath': file.filepath
        } for file in files]
        return jsonify({'files': files_data})
    return jsonify({'message': 'Not authenticated'})

@app.route('/register', methods=['POST'])
def register():
    if current_user.is_authenticated:
        return jsonify({'message': 'Already authenticated'})

    data = request.get_json()
    form = RegistrationForm(data=data)
    if form.validate():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Registration successful'})
    else:
        errors = form.errors
        return jsonify({'errors': errors}), 400

@app.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return jsonify({'message': 'Already authenticated'})

    data = request.get_json()
    form = LoginForm(data=data)
    if form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    else:
        errors = form.errors
        return jsonify({'errors': errors}), 400

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'})

@app.route('/profile', methods=['GET'])
@login_required
def profile():
    return jsonify({
        'username': current_user.username,
        'email': current_user.email,
        'premium': current_user.premium
    })

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if not current_user.premium:
        user_file_count = FileStorage.query.filter_by(user_id=current_user.id).count()
        if user_file_count >= 3:
            return jsonify({'message': 'Non-premium users can upload up to 3 files only'}), 403

    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        filepath = os.path.join('backend', 'uploads', filename)
        file.save(filepath)

        file_storage = FileStorage(filename=filename, filepath=filepath, user_id=current_user.id)
        db.session.add(file_storage)
        db.session.commit()

        return jsonify({'message': 'File successfully uploaded'})
    else:
        errors = form.errors
        return jsonify({'errors': errors}), 400

@app.route('/uploads/<filename>', methods=['GET'])
@login_required
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

@app.route('/delete/<int:file_id>', methods=['DELETE'])
@login_required
def delete_file(file_id):
    file = FileStorage.query.get_or_404(file_id)

    if os.path.exists(file.filepath):
        os.remove(file.filepath)

    db.session.delete(file)
    db.session.commit()

    return jsonify({'message': 'File deleted successfully'})

@app.route('/buy_premium', methods=['POST'])
@login_required
def buy_premium():
    access_token = get_payu_access_token()
    if not access_token:
        return jsonify({'message': 'Failed to obtain access token from PayU'}), 500

    order_data = {
        "notifyUrl": app.config['PAYU_NOTIFY_URL'],
        "customerIp": request.remote_addr,
        "merchantPosId": app.config['PAYU_CLIENT_ID'],
        "description": "Premium Membership",
        "currencyCode": "PLN",
        "totalAmount": "1000",
        "products": [
            {
                "name": "Premium Membership",
                "unitPrice": "1000",
                "quantity": "1"
            }
        ],
        "buyer": {
            "email": current_user.email,
            "firstName": current_user.username,
            "language": "pl"
        },
        "continueUrl": app.config['PAYU_CONTINUE_URL']
    }

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.post(
        f"{app.config['PAYU_API_URL']}/api/v2_1/orders",
        json=order_data,
        headers=headers,
        allow_redirects=False  # Disable automatic redirect handling
    )

    logging.debug(f'PayU response headers: {response.headers}')
    logging.debug(f'PayU response status code: {response.status_code}')
    logging.debug(f'PayU response content: {response.content}')

    if response.status_code in (200, 201):
        return jsonify({'redirectUri': response.json().get('redirectUri')})
    elif response.status_code == 302:
        return jsonify({'redirectUri': response.headers.get('Location')})
    else:
        return jsonify({'message': 'There was an error with the payment gateway'}), 500

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    logging.debug(f'PayU notification received: {data}')
    print(data)
    if data['order']['status'] == 'COMPLETED':
        user = User.query.filter_by(email=data['order']['buyer']['email']).first()
        if user:
            user.premium = True
            db.session.commit()
            logging.info(f'User {user.email} has been upgraded to premium.')
        else:
            logging.warning(f'User with email {data["order"]["buyer"]["email"]} not found.')
    else:
        logging.warning(f'Order status is not completed: {data["order"]["status"]}')

    return jsonify({'status': 'ok'})

# Obsługa plików statycznych
@app.route('/static/<path:path>', methods=['GET'])
def send_static(path):
    return send_from_directory('static', path)
