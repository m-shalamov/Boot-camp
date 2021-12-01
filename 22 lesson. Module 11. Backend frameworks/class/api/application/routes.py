from flask import Blueprint, jsonify, request

from application.app import db
from application.database import User

view = Blueprint("view", __name__)


@view.route("/")
def home():
    return "Hello!"


@view.route("/users/<name>")
def get_data(name):
    user = User.query.filter_by(name=name).first()
    user.count += 1
    db.session.commit()
    return jsonify({"name": user.name, "count": user.count})


@view.route("/user", methods=["POST"])
def add():
    data = request.json
    user = User(name=data["name"], count=data["count"])
    db.session.add(user)
    db.session.commit()
    return jsonify(data)
