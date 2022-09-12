from flask import jsonify, request
from flask_login import current_user

from . import api

from src.models import (
    db, Purchase
)
from src.config import logger


@api.route('/purchases', methods=["GET"])
def get_all_purchases():
    purchs = Purchase(db)
    purchases = purchs.get_all()
    return jsonify(purchases)


@api.route("/purchase", methods=["POST"])
def new_purchase():
    purchase_data = request.form.to_dict()
    purchase_data["means_of_payment_id"] = purchase_data["means_of_payment"]
    purchase_data["number_of_payments"] = purchase_data["payments_count"]
    # purchase_data["payment_number"] = 1
    purchase_data["date"] = purchase_data["purchase_date"]
    purchase_data["category_id"] = purchase_data["category"]
    purchase_data["user_id"] = current_user.id
    logger.info(purchase_data)
    purchase = Purchase(db)
    new_id = purchase.save(purchase_data)
    return jsonify(new_id)
