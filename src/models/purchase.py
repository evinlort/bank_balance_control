import calendar

from psycopg2 import sql

from src.helpers.calculation_helpers import calculate_monthly_sums, calculate_next_month_date
from src.models.base_model import BaseModel


class Purchase(BaseModel):
    @staticmethod
    def get_table():
        return "purchases"

    def get_by_month_and_year(self, month: int, year: int, user_id: int = None):
        user = "" if not user_id else "AND user_id = %(user_id)s"
        query = sql.SQL(
            """
            SELECT * FROM {} 
            WHERE date >= '%(year)s-%(month)s-01' 
            AND date <= '%(year)s-%(month)s-%(month_last_day)s'
            {}
            ORDER BY date ASC
            """.format(self.table, user)
        )

        month_last_day = calendar.monthrange(year, month)[1]
        data = {"year": year, "month": month, "month_last_day": month_last_day, "user_id": user_id}
        self.logger.debug(query)

        self.logger.debug(self.db.cursor.mogrify(query, data))
        self.db.cursor.execute(query, data)
        self.db.connection.commit()
        fetch = self.db.cursor.fetchall()
        self.logger.debug(fetch)
        if fetch is None:
            return []
        return self.convert(fetch)

    def get_by_userid_month_and_year(self, user_id: int, month: int, year: int):
        query = sql.SQL(
            """
            SELECT * FROM {} 
            WHERE date >= '%(year)s-%(month)s-01' 
            AND date <= '%(year)s-%(month)s-%(month_last_day)s'
            AND user_id = %(user_id)s
            ORDER BY date ASC
            """.format(self.table)
        )

        month_last_day = calendar.monthrange(year, month)[1]
        data = {"user_id": user_id, "year": year, "month": month, "month_last_day": month_last_day}
        self.logger.debug(query)

        self.logger.debug(self.db.cursor.mogrify(query, data))
        self.db.cursor.execute(query, data)
        self.db.connection.commit()
        fetch = self.db.cursor.fetchall()
        self.logger.debug(fetch)
        if fetch is None:
            return []
        return self.convert(fetch)

    def save(self, purchase_data):
        if int(purchase_data["number_of_payments"]) > 1:
            monthly_sums = calculate_monthly_sums(
                float(purchase_data["sum"]),
                int(purchase_data["number_of_payments"])
            )
            for payment_number in range(1, int(purchase_data["number_of_payments"]) + 1):
                purchase_data["sum"] = monthly_sums[payment_number - 1]
                purchase_data["payment_number"] = payment_number
                super().save(data_to_save=purchase_data)
                purchase_data["date"] = calculate_next_month_date(purchase_data["date"])
        else:
            purchase_data["payment_number"] = 1
            super().save(data_to_save=purchase_data)
