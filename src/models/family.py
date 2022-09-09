import psycopg2.errors
from psycopg2 import sql

from src.models.name import Name
from src.models.translation import Translation
from src.models.base_model import BaseModel


class Family(BaseModel):
    @staticmethod
    def get_table():
        return "families"

    def save(self, row):
        query = sql.SQL("SELECT * FROM {}".format(self.table))
        self.logger.info(self.db.cursor.mogrify(query, row))
        try:
            self.db.cursor.execute(query, row)
            self.db.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.db.connection.rollback()

        return self.db.cursor.fetchone()[0]
