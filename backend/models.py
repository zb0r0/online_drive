from backend.app import db
from flask_login import UserMixin
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    premium = db.Column(db.Boolean, default=False)
    files = db.relationship('FileStorage', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class FileStorage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"File('{self.filename}')"

#schematy serializacji
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        exclude = ('password',)  # Exclude password from the serialized output

class FileStorageSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FileStorage
        include_fk = True
        load_instance = True
