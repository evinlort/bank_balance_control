from flask import jsonify

from . import api

from src.models import (
    db, Category
)


@api.route('/categories', methods=["GET"])
def get_all_categories():
    cat = Category(db)
    categories = cat.get_all_categories()
    return jsonify(categories)


@api.route('/currency/<_id>', methods=["GET"])
def get_category(_id):
    cat = Category(db)
    category = cat.get_by_id(_id)
    return jsonify(category)
