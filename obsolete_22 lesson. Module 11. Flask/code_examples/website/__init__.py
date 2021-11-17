from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = '2688088b53e6e0116a1ddb59f72db9d1'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///website.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from website import routes