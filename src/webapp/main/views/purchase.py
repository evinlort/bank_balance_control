import calendar
import datetime

from flask import render_template
from flask_login import login_required, current_user

from src.helpers.models_helper import add_object_by_name
from src.models import (
    db, Purchase, User,
)
from src.webapp.main import main


@main.route('/purchases', methods=["GET"])
@login_required
def show_purchases():
    purchase = Purchase(db)
    this_user = current_user.__dict__

    this_user["family_members"] = None
    if this_user["family_id"]:
        this_user["family_members"] = User(db).get_by_column("family_id", this_user["family_id"])

    current_date = datetime.datetime.now()
    month = current_date.month
    year = current_date.year
    month_last_day = calendar.monthrange(year, month)[1]

    purchases = purchase.get_by_month_and_year(month, year, month_last_day)
    add_object_by_name(db, "means_of_payment", purchases)
    add_object_by_name(db, "category", purchases)
    add_object_by_name(db, "user", purchases)

    current_date = datetime.datetime.now()
    month_name = current_date.strftime("%B")

    params = {
        "purchases": purchases,
        "month": month_name,
        "year": year,
        "current_user": this_user,
        "total_sum": "{:.2f}".format(round(sum([float(item["sum"][1:]) for item in purchases]), 2)),
    }
    return render_template("/purchases/purchases.html", params=params)
