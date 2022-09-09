from psycopg2 import sql

from src.config import logger
from src.webapp import db


class BaseModel:
    def __init__(self, dbp=None):
        if dbp:
            self.db = dbp
        else:
            self.db = db
        self.logger = logger

    @property
    def table(self):
        table_method = getattr(self, "get_table", None)
        if callable(table_method):
            return table_method()
        raise NotImplemented

    @staticmethod
    def convert_to_dicts_in_list(fetch_list: list) -> list:
        resulting_list = []
        for fetch_dict in fetch_list:
            resulting_list.append(dict(fetch_dict))
        return resulting_list

    def get_all(self) -> list:
        query = sql.SQL("""
                SELECT * FROM {};
        """.format(self.table)
        )

        self.logger.info(self.db.cursor.mogrify(query))
        self.db.cursor.execute(query)
        fetch = self.db.cursor.fetchall()
        if fetch is None:
            return []
        return self.convert_to_dicts_in_list(fetch)

    def get_by_id(self, _id: int) -> dict:
        query = sql.SQL("""
                SELECT * FROM {}
                WHERE id = %s;
        """.format(self.table)
        )

        params = (_id, )
        self.logger.info(self.db.cursor.mogrify(query, params))
        self.db.cursor.execute(query, params)
        fetch = self.db.cursor.fetchone()
        if fetch is None:
            return {}
        return fetch

    def get_by_column(self, column_name, column_value):
        query = sql.SQL("""
                SELECT * FROM {}
                WHERE {} = %s;
        """.format(self.table, column_name)
        )

        params = (column_value, )
        self.logger.info(self.db.cursor.mogrify(query, params))
        self.db.cursor.execute(query, params)
        fetch = self.db.cursor.fetchall()
        if fetch is None:
            return []
        return self.convert(fetch)

    @staticmethod
    def convert(fetch):
        if isinstance(fetch, list):
            return [dict(entry) for entry in fetch]
        return dict(fetch)
