from flask_login import UserMixin

from src.webapp import login_manager
from src.config import logger
from src.models.base_model import BaseModel
from psycopg2 import sql


class User(UserMixin, BaseModel):
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

    def get_by_credentials(self, username, password):
        query = sql.SQL(f"""
                    SELECT * from users where username = '{username}'
                    AND password_hash = '{password}'
                """)
        logger.debug(query)
        self.db.cursor.execute(query)
        fetch = self.db.cursor.fetchone()
        logger.debug(dict(fetch))
        if not fetch:
            return {}
        return fetch

    def get_user_for_login(self, username, password):
        user = self.get_by_credentials(username, password)
        u = self.__dict__.update(user)
        return u

    def get_by_id_for_login(self, user_id):
        query = sql.SQL(f"""
                    SELECT * from users where id = '{user_id}'
                """)
        self.db.cursor.execute(query)
        fetch = self.db.cursor.fetchone()
        if not fetch:
            return
        self.__dict__.update(fetch)
        return self


@login_manager.user_loader
def load_user(user_id):
    u = User()
    u.get_by_id_for_login(user_id)
    return u
