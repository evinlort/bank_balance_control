from psycopg2 import sql

from src.models.base_model import BaseModel


class Balance(BaseModel):
    table = "balances"

    def get_by_month(self, month):
        query = sql.SQL(f"""
            SELECT * from balances where month = '{month}'
        """)

        self.db.cursor.execute(query)
        fetch = self.db.cursor.fetchone()
        if fetch is None:
            return {}
        return fetch
