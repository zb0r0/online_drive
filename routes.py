import os
import requests
from flask import render_template, url_for, redirect, flash, request, send_from_directory, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from app import app, db, login_manager
from models import User, FileStorage
from forms import RegistrationForm, LoginForm, UploadFileForm
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
        return render_template("index.html", files=files)
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)
        file.save(filepath)

        file_storage = FileStorage(filename=filename, filepath=filepath, user_id=current_user.id)
        db.session.add(file_storage)
        db.session.commit()

        flash('File successfully uploaded', 'success')
        return redirect(url_for('home_page'))
    return render_template('upload.html', form=form)

@app.route('/uploads/<filename>')
@login_required
def uploaded_file(filename):
    return send_from_directory('uploads', filename)


@app.route('/delete/<int:file_id>', methods=['POST'])
@login_required
def delete_file(file_id):
    file = FileStorage.query.get_or_404(file_id)

    if os.path.exists(file.filepath):
        os.remove(file.filepath)

    db.session.delete(file)
    db.session.commit()

    flash('File deleted successfully', 'success')
    return redirect(url_for('home_page'))

@app.route('/buy_premium', methods=['POST'])
@login_required
def buy_premium():
    access_token = get_payu_access_token()
    if not access_token:
        flash('Failed to obtain access token from PayU', 'danger')
        return redirect(url_for('profile'))

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
        return redirect(response.json().get('redirectUri'))
    elif response.status_code == 302:
        return redirect(response.headers.get('Location'))
    else:
        flash('There was an error with the payment gateway.', 'danger')
        return redirect(url_for('profile'))

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    # Verify the notification here with PayU if needed
    if data['order']['status'] == 'COMPLETED':
        user = User.query.filter_by(email=data['order']['buyer']['email']).first()
        if user:
            user.is_premium = True
            db.session.commit()
    return jsonify({'status': 'ok'})