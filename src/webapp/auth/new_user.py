import hashlib

from flask import request, jsonify

from . import auth
from src.config import logger
from src.models import db, User


@auth.route("/new_user", methods=["POST"])
def new_user():
    new_user_data = request.form.to_dict()
    logger.debug(new_user_data)

    pass_hash = hashlib.new("sha1", new_user_data["password"].encode())
    new_user_data["password_hash"] = pass_hash.hexdigest()

    logger.debug(new_user_data)
    user = User(db)
    new_id = user.save(new_user_data)
    return jsonify(new_id)
