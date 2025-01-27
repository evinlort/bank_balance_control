import os

import psycopg2
from psycopg2.extras import DictCursor

database_name = os.getenv("DATABASE")


class DBConnect:
    def __init__(self):
        self.connection = psycopg2.connect(f"dbname={database_name} user={os.getenv('USER')}")
        self.cursor = self.connection.cursor(cursor_factory=DictCursor)

    def init_app(self, app):
        app.db = self
        return app


db = DBConnect()
