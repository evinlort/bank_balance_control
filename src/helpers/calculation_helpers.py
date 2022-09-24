import datetime
from decimal import Decimal
from typing import List

from dateutil.relativedelta import relativedelta


def calculate_next_month_date(date: str) -> str:
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    next_month_date_obj = date_obj + relativedelta(months=1)
    return next_month_date_obj.strftime("%Y-%m-%d")


def calculate_monthly_sums(general_sum: float, payments: int) -> List[float]:
    rounded_month_sum = int(general_sum / payments * 100) / 100
    first_month_sum = round(general_sum - round(rounded_month_sum * (payments - 1), 2), 2)
    calculated_sums = []
    for i in range(0, payments):
        if i == 0:
            calculated_sums.append(first_month_sum)
            continue
        calculated_sums.append(rounded_month_sum)
    return calculated_sums
