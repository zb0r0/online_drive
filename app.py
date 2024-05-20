from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = '123secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@DESKTOP-DJ1UNI3/online_drive?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    files = db.relationship('FileStorage', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class FileStorage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.filename}')"

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
