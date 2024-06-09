import os
from flask import request, jsonify
from flask_restful import Api, Resource
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from backend.app import app, db
from backend.models import User, FileStorage, UserSchema, FileStorageSchema
import logging

logging.basicConfig(level=logging.DEBUG)

api = Api(app)

# Schematy serializacji
user_schema = UserSchema()
users_schema = UserSchema(many=True)
file_schema = FileStorageSchema()
files_schema = FileStorageSchema(many=True)

# Resource for handling users
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        data = request.json
        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        user = User(username=data['username'], email=data['email'], password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201

# Resource for handling file storage
class FileResource(Resource):
    @login_required
    def get(self, file_id):
        file = FileStorage.query.get_or_404(file_id)
        return file_schema.dump(file)

    @login_required
    def delete(self, file_id):
        file = FileStorage.query.get_or_404(file_id)
        if os.path.exists(file.filepath):
            os.remove(file.filepath)
        db.session.delete(file)
        db.session.commit()
        return '', 204

class FileListResource(Resource):
    @login_required
    def get(self):
        files = FileStorage.query.filter_by(user_id=current_user.id).all()
        return files_schema.dump(files)

    @login_required
    def post(self):
        data = request.form
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join('backend', 'uploads', filename)
        file.save(filepath)
        file_storage = FileStorage(filename=filename, filepath=filepath, user_id=current_user.id)
        db.session.add(file_storage)
        db.session.commit()
        return file_schema.dump(file_storage), 201

# Adding routes to the API
api.add_resource(UserListResource, '/api/users')
api.add_resource(UserResource, '/api/users/<int:user_id>')
api.add_resource(FileListResource, '/api/files')
api.add_resource(FileResource, '/api/files/<int:file_id>')
