from urllib import request

import structlog
import base64
from flask import Blueprint, jsonify, request

from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import JWTManager

from db_utils import db
from models.user import User

auth_blue_print = Blueprint('auth', __name__)

logger = structlog.get_logger(__name__)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@auth_blue_print.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # password in db is encoded
    password = str(base64.b64decode(password))
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        text_response = "Login successfully"
        logger.info(text_response)
        access_token = create_access_token(identity=email, fresh=True)
        refresh_token = create_refresh_token(identity=email)
        return jsonify(access_token=access_token, refresh_token=refresh_token)
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@auth_blue_print.route("/sign-up", methods=["POST"])
def sign_up():
    email = request.json.get("email", None)
    user = User.query.filter_by(email=email).first()
    if user:
        text_response = "email already existed"
        logger.info(text_response)
        return jsonify({"msg": text_response}), 400

    password = request.json.get("password", None)
    user = User(email=email, password=str(base64.b64decode(password)))
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created!"}), 201
