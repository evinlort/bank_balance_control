from flask import render_template
from flask_login import login_required, current_user

from src.config import logger
from src.helpers.models_helper import add_object_by_name
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
    add_object_by_name(db, "user", purchases)
    add_object_by_name(db, "category", purchases)

    logger.debug(purchases)
    params = {"purchases": purchases}
    return render_template("/purchases/purchases.html", params=params)
