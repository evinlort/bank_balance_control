from flask import jsonify, request
from flask_login import current_user

from src.config import logger
from . import api
from ...helpers.calculation_helpers import calculate_monthly_sums


@api.route('/calculate/sum/<purchase_sum>/payments/<payments>/first_payment', methods=["GET"])
def calculate_first_payment(purchase_sum, payments):
    return jsonify({"first_payment": calculate_monthly_sums(float(purchase_sum), int(payments))[0]})
