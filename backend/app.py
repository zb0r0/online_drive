from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_folder='static')
app.config.from_object('backend.config.Config')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from backend.models import User
from backend.routes import *

if not os.path.exists('backend/uploads'):
    os.makedirs('backend/uploads')

if __name__ == '__main__':
    app.run(debug=True)
