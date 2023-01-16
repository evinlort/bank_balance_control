
from flask import jsonify, request, render_template
from flask_login import current_user, login_required

from src.config import logger
from . import api

from src.models import (
    db, Category, HistoryOfBalance
)


@api.route('/categories', methods=["GET"])
@login_required
def get_all_family_categories():
    cat = Category(db)
    logger.error(current_user.__dict__)
    categories = cat.get_all_family_categories(family_id=current_user.family_id)
    return jsonify(categories)


@api.route('/category', methods=["POST"])
@login_required
def add_category():
    new_cat_name = request.form.get("category_name")
    cat = Category(db)
    to_insert = {"name": new_cat_name, "family_id": current_user.family_id}
    new_id = cat.save(to_insert)
    return jsonify({"new_id": new_id})


@api.route('/category/<_id>', methods=["PATCH"])
@login_required
def edit_category(_id: str):
    _id = int(_id)
    cat_balance_edited = 0

    req_json = request.get_json()
    cat_name_edited = req_json["category_name"]  # mandatory
    if "category_balance" in req_json:
        cat_balance_edited = request.get_json()["category_balance"]
    cat = Category(db)
    category = cat.get_by_id(_id)
    prev_balance = category["balance"]

    # https://docs.google.com/document/d/1rbyjtXea9o4U7WFt91meBLjQ8dyZ4QKxORpReZ-AiMg/edit#bookmark=id.4p4xuzcvodtz)
    if prev_balance:
        history_of_balance = HistoryOfBalance(db)
        history_of_balance.save({"category_id": _id, "previous_balance": prev_balance})

    to_update = {"name": cat_name_edited, "balance": cat_balance_edited}
    updated_id = cat.update(_id, to_update)
    return jsonify({"updated_id": updated_id})


@api.route('/category/<int:_id>', methods=["GET"])
@login_required
def fetch_category(_id: int):
    cat = Category(db)
    category = cat.get_by_id(_id=_id)
    return jsonify({"category": category})
