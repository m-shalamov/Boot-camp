import os

import config
from flask import Flask


def create_app(db):
    app = Flask(__name__)
    flask_env = os.getenv("FLASK_ENV", None)
    if flask_env == "development":
        app.config.from_object(config.DevelopmentConfig)
    elif flask_env == "testing":
        app.config.from_object(config.TestingConfig)
    elif flask_env == "production":
        app.config.from_object(config.ProductionConfig)

    db.init_app(app)

    from application.routes import view

    app.register_blueprint(view)
    return app
