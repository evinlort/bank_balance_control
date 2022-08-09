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
    month_number = current_date.strftime("%m")
    month_name = current_date.strftime("%B")

    balance = Balance().get_by_month(month=month_number)
    params = {
        "rand": random.randrange(1111, 9999),
        "user": user,
        "balance": balance,
        "current_month_name": month_name,
    }
    return render_template("/home/index.html", params=params)
