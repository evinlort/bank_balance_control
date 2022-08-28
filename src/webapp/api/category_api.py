from flask import jsonify, request

from . import api

from src.models import (
    db, Category
)


@api.route('/categories', methods=["GET"])
def get_all_categories():
    cat = Category(db)
    categories = cat.get_all_categories()
    return jsonify(categories)


@api.route('/category', methods=["POST"])
def add_category():
    new_cat_name = request.form.get("category_name")
    language_id = request.form.get("language_id")
    cat = Category(db)
    # category = cat.get_by_id()
    return jsonify(True)  # {"LANG": language_id, "NAME": new_cat_name})
