import datetime

from flask import render_template
from flask_login import login_required, current_user

from src.helpers.models_helper import add_object_by_name
from src.models import (
    db, Purchase, User,
)
from src.webapp.main import main


@main.route('/purchases', methods=["GET"])
@main.route('/purchases/user/<int:user_id>', methods=["GET"])
@main.route('/purchases/user/<int:user_id>/month/<int:month>/year/<int:year>', methods=["GET"])
@login_required
def show_purchases(user_id: int = None, month: int = None, year: int = None):
    purchase = Purchase(db)
    this_user = current_user.__dict__

    this_user["family_members"] = None
    if this_user["family_id"]:
        this_user["family_members"] = User(db).get_by_column("family_id", this_user["family_id"])

    current_date = datetime.datetime.now()
    if not month:
        month = current_date.month
    if not year:
        year = current_date.year

    purchases = purchase.get_by_month_and_year(month, year, user_id=user_id)
    add_object_by_name(db, "means_of_payment", purchases)
    add_object_by_name(db, "category", purchases)
    add_object_by_name(db, "user", purchases)

    current_date = datetime.datetime.now()
    month_name = current_date.strftime("%B")

    params = {
        "purchases": purchases,
        "month": month_name,
        "month_number": month,
        "year": year,
        "current_user": this_user,
        "total_sum": "{:.2f}".format(round(sum([float(item["sum"][1:]) for item in purchases]), 2)),
    }
    return render_template("/purchases/purchases.html", params=params)
