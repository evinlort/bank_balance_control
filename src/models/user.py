from src.models.base_model import BaseModel
from psycopg2 import sql


class User(BaseModel):
    table = "users"

    def fetch_by_username(self, username):
        query = sql.SQL(f"""
            SELECT * from users where username = '{username}'
        """)

        print(self.db.cursor.mogrify(query))
        self.db.cursor.execute(query)
        fetch = self.db.cursor.fetchone()
        if fetch is None:
            return {}
        return fetch
