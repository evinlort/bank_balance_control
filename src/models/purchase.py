import datetime

from src.models.base_model import BaseModel
from dateutil.relativedelta import relativedelta


class Purchase(BaseModel):
    @staticmethod
    def get_table():
        return "purchases"

    def save(self, purchase_data):
        if int(purchase_data["number_of_payments"]) > 1:
            monthly_sum = float(purchase_data["sum"]) / int(purchase_data["number_of_payments"])
            for payment_number in range(1, purchase_data["number_of_payments"] + 1):
                purchase_data["payment_number"] = payment_number
                super().save(data_to_save=purchase_data)
                purchase_data["date"] = self.calculate_next_month_date(purchase_data["date"])
        else:
            super().save(data_to_save=purchase_data)

    @staticmethod
    def calculate_next_month_date(date: str) -> str:
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        next_month_date_obj = date_obj + relativedelta(months=1)
        return next_month_date_obj.strftime("%Y-%m-%d")
