from flask import jsonify

from . import api

from src.models import (
    db, Currency
)


@api.route('/currencies', methods=["GET"])
def get_all_currencies():
    curr = Currency(db)
    currencies = curr.get_all()
    print(currencies)
    return jsonify(currencies)


@api.route('/currency/<_id>/sign', methods=["GET"])
def get_all_currencies(_id):
    curr = Currency(db)
    currency = curr.get_by_id(_id)
    print(currency)
    return jsonify(sign)
