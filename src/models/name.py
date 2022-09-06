import psycopg2.errors
from psycopg2 import sql

from src.models.base_model import BaseModel


class Name(BaseModel):
    @staticmethod
    def get_table():
        return "names"

    def save(self, row):
        query = sql.SQL("INSERT INTO {} "
                        "(name) "
                        "VALUES (%(name)s) "
                        "RETURNING id".format(self.table, self.table))
        self.logger.info(self.db.cursor.mogrify(query, row))
        try:
            self.db.cursor.execute(query, row)
            self.db.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.db.connection.rollback()
            query = sql.SQL("SELECT id FROM {} WHERE name = %(name)s".format(self.table))
            self.db.cursor.execute(query, row)

        return self.db.cursor.fetchone()[0]

