from psycopg2 import sql

from src.models.base_model import BaseModel


class Translation(BaseModel):
    @staticmethod
    def get_table():
        return "translations"

    def get_by_name_id_and_language(self, name_id: int, language_id: int) -> dict:
        query = sql.SQL("""
            SELECT * FROM {}
            WHERE name_id = %s
            AND language_id = %s
        """).format(sql.Identifier(self.table))

        params = (name_id, language_id)
        self.logger.info(self.db.cursor.mogrify(query, params))
        self.db.cursor.execute(query, params)
        fetch = self.db.cursor.fetchone()
        if fetch is None:
            return {}
        return fetch
