from psycopg2 import sql

from src.models.base_model import BaseModel


class Balance(BaseModel):
    table = "balances"

    def get_by_month_year(self, month, year):
        query = sql.SQL(f"""
            SELECT * FROM balances
            WHERE month = {month}
            AND year = {year}
        """)

        self.db.cursor.execute(query)
        fetch = self.db.cursor.fetchall()
        if fetch is None:
            return []
        return fetch
        # return self.convert_to_dicts_in_list(fetch)
