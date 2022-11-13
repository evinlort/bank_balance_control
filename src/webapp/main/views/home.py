import datetime
import random
import sys

from flask import redirect, url_for, flash, render_template
from flask_login import login_required, current_user

from src.models.balance import Balance
from src.webapp.main import main
from src.config import logger


@main.route('/', methods=["GET"])
@login_required
def home_page():
    user = current_user
    current_date = datetime.datetime.now()
    year = current_date.strftime("%Y")
    month_number = current_date.strftime("%m")
    month_name = current_date.strftime("%B")

    # balances = Balance().get_by_month_year(month=month_number, year=year)
    balances = [{"defined": 0, "current": 0}]
    balance = {
        "defined": sum([balance["defined"] for balance in balances]),
        "current": sum([balance["current"] for balance in balances])
    }
    params = {
        "rand": random.randrange(1111, 9999),
        "user": user,
        "balance": balance,
        "current_month_name": month_name,
    }
    return render_template("/home/index.html", params=params)
