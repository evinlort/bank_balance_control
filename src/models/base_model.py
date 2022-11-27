import time
from typing import Union, List

import psycopg2.errors
from psycopg2 import sql

from src.config import logger
from src.decorators import validate_attributes
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
        return self.convert(fetch)

    def get_by_id(self, _id: int) -> dict:
        query = sql.SQL("""
                SELECT * FROM {}
                WHERE id = %s;
        """.format(self.table)
                        )

        params = (_id,)
        self.logger.info(self.db.cursor.mogrify(query, params))
        self.db.cursor.execute(query, params)
        fetch = self.db.cursor.fetchone()
        if fetch is None:
            return {}
        return fetch

    def get_by_column(self, column_name: str, column_value: str) -> list:
        query = sql.SQL("""
                SELECT * FROM {}
                WHERE {} = %s;
        """.format(self.table, column_name)
                        )

        params = (column_value,)
        self.logger.info(self.db.cursor.mogrify(query, params))
        self.db.cursor.execute(query, params)
        fetch = self.db.cursor.fetchall()
        if fetch is None:
            return []
        return self.convert(fetch)

    def save(self, data_to_save: dict) -> int:
        try:
            raw_table_columns = self.get_table_columns()
            to_insert_columns = []
            to_save_values = []
            for col in raw_table_columns:
                if self.get_type_by_column_name(col) == "timestamp":
                    continue
                if self.get_type_by_column_name(col) == "numeric":
                    if col not in data_to_save:
                        data_to_save[col] = 0
                to_insert_columns.append(col)
                to_save_values.append(str(data_to_save[col]) if col in data_to_save else 'NULL')

            self.logger.info(to_save_values)

            query = sql.SQL(
                "INSERT INTO {} ({}) VALUES ({}) RETURNING id".format(
                    self.table,
                    sql.SQL(', ').join(
                        [sql.Identifier(col_name) for col_name in to_insert_columns]
                    ).as_string(self.db.cursor),
                    sql.SQL(', ').join(
                        sql.Placeholder() * len(to_save_values)
                    ).as_string(self.db.cursor)
                ))
            self.logger.info(self.db.cursor.mogrify(query, to_save_values))
            self.db.cursor.execute(query, to_save_values)
            self.db.connection.commit()
            fetch = self.db.cursor.fetchone()
            if fetch is None:
                return 0
            return fetch["id"]
        except psycopg2.errors.UniqueViolation as pg_uniq:
            self.db.connection.rollback()
            self.logger.error(str(pg_uniq))
            return -1
        except psycopg2.errors.InvalidTextRepresentation as itr:
            if "invalid input syntax for type" in str(itr) and '"None"' in str(itr):
                self.db.connection.rollback()
                self.logger.error("There is NULL value given for the 'not null' field")
                return -2

    @validate_attributes
    def update(self, _id: str, data: dict) -> int:
        raise NotImplemented

    def get_table_columns(self) -> list:
        query = sql.SQL("SELECT * FROM {}".format(self.table))
        self.db.cursor.execute(query)
        return [desc[0] for desc in self.db.cursor.description if desc[0] != "id"]

    def get_type_by_column_name(self, column_name: str) -> str:
        query = sql.SQL("SELECT * FROM {}".format(self.table))
        self.db.cursor.execute(query)
        for column in self.db.cursor.description:
            if column[0] == column_name:
                return self.get_type_code_name(column[1]).lower()

    def get_type_code_name(self, type_code: Union[int, str]) -> str:
        query = sql.SQL("SELECT typname FROM pg_type WHERE oid = %s")
        self.db.cursor.execute(query, (type_code,))
        fetch = self.db.cursor.fetchone()
        if fetch is None:
            return ""
        return fetch["typname"]

    @staticmethod
    def convert(fetch: Union[list, dict]) -> Union[List[dict], dict]:
        if isinstance(fetch, list):
            return [dict(entry) for entry in fetch]
        return dict(fetch)
