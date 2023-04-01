from flask import render_template
from flask_login import login_required, current_user

from src.config import logger
from src.models import (
    db, Purchase,
)
from src.webapp.main import main


@main.route('/purchases', methods=["GET"])
@login_required
def show_purchases():
    purchase = Purchase(db)
    logger.error(current_user.__dict__)
    purchases = purchase.get_all()
    logger.info(purchases)
    params = {"purchases": purchases}
    return render_template("/purchases/purchases.html", params=params)
