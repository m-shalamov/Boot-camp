from flask_sqlalchemy import SQLAlchemy
from application import create_app

db = SQLAlchemy()
app = create_app(db)

with app.app_context():
    db.create_all()
