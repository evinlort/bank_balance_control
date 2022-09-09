from flask import jsonify

from src.config import logger
from . import api

from src.models import (
    db, MeansOfPayment
)


@api.route('/means_of_payments', methods=["GET"])
def get_all_means_of_payment():
    means = MeansOfPayment(db)
    means_of_payments = means.get_all()
    return jsonify(means_of_payments)
