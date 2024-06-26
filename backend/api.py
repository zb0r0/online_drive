import os
from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_cors import CORS
import logging
import jwt
import datetime
from functools import wraps
from backend.app import app, db
from backend.models import User, FileStorage, UserSchema, FileStorageSchema
from sqlalchemy.exc import IntegrityError

logging.basicConfig(level=logging.DEBUG)

api = Api(app)
CORS(app)

# Schematy serializacji
user_schema = UserSchema()
users_schema = UserSchema(many=True)
file_schema = FileStorageSchema()
files_schema = FileStorageSchema(many=True)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            token = token.split(" ")[1]
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['user_id']).first()
            if current_user is None:
                raise Exception('User not found')
        except Exception as e:
            logging.error(f"Token is invalid: {e}")
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user=current_user, *args, **kwargs)

    return decorated

# Resource for handling users
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user_schema.dump(user))

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return jsonify(users_schema.dump(users))

    def post(self):
        data = request.json
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'Email already exists'}), 400

        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        user = User(username=data['username'], email=data['email'], password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            logging.error(f"IntegrityError: {e}")
            return jsonify({'message': 'An error occurred while creating the user.'}), 500
        except Exception as e:
            db.session.rollback()
            logging.error(f"Exception: {e}")
            return jsonify({'message': 'An unexpected error occurred.'}), 500

        return jsonify(user_schema.dump(user)), 201

# Resource for handling file storage
class FileResource(Resource):
    @token_required
    def get(self, current_user, file_id):
        file = FileStorage.query.get_or_404(file_id)
        return jsonify(file_schema.dump(file))

    @token_required
    def delete(self, current_user, file_id):
        file = FileStorage.query.get_or_404(file_id)
        if os.path.exists(file.filepath):
            os.remove(file.filepath)
        db.session.delete(file)
        db.session.commit()
        return '', 204

class FileListResource(Resource):
    @token_required
    def get(self, current_user):
        files = FileStorage.query.filter_by(user_id=current_user.id).all()
        return jsonify(files_schema.dump(files))

    @token_required
    def post(self, current_user):
        data = request.form
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join('backend', 'uploads', filename)
        file.save(filepath)
        file_storage = FileStorage(filename=filename, filepath=filepath, user_id=current_user.id)
        db.session.add(file_storage)
        db.session.commit()
        return jsonify(file_schema.dump(file_storage)), 201

class LoginResource(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, app.config['SECRET_KEY'], algorithm='HS256')
            logging.info('Login successful for user: %s', email)
            return jsonify({'message': 'Logged in successfully', 'token': token, 'userId': user.id})
        else:
            logging.warning('Invalid login attempt for user: %s', email)
            return jsonify({'message': 'Invalid credentials'}), 401

# Adding routes to the API
api.add_resource(UserListResource, '/api/users')
api.add_resource(UserResource, '/api/users/<int:user_id>')
api.add_resource(FileListResource, '/api/files')
api.add_resource(FileResource, '/api/files/<int:file_id>')
api.add_resource(LoginResource, '/api/login')