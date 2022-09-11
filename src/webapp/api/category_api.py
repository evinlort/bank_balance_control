from datetime import datetime

from flask import jsonify, request
from flask_login import current_user

from src.config import logger
from . import api

from src.models import (
    db, Category
)


@api.route('/categories', methods=["GET"])
def get_all_family_categories():
    cat = Category(db)
    categories = cat.get_all_family_categories(family_id=current_user.family_id)
    return jsonify(categories)


@api.route('/category', methods=["POST"])
def add_category():
    new_cat_name = request.form.get("category_name")
    cat = Category(db)
    to_insert = {"name": new_cat_name, "family_id": current_user.family_id}
    new_id = cat.save(to_insert)
    return jsonify({"new_id": new_id})
