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


@api.route('/category/<_id>', methods=["PATCH"])
def edit_category(_id: str):
    cat_name_edited = request.get_data(as_text=True).split("=")[1]
    cat = Category(db)
    to_update = {"name": cat_name_edited}
    updated_id = cat.update(_id, to_update)
    return jsonify({"updated_id": updated_id})
