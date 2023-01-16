from psycopg2 import sql

from src.models.base_model import BaseModel


class Category(BaseModel):
    @staticmethod
    def get_table():
        return "categories"

    def get_all_family_categories(self, family_id) -> list:
        categories = self.get_by_column("family_id", family_id)
        return categories

    def update(self, _id: int, data: dict) -> int:
        query = sql.SQL("UPDATE {} SET {} WHERE id=%(id)s RETURNING id".format(self.table, sql.SQL(', ').join(
                    [
                        sql.SQL(key+"=") + sql.Placeholder(key) for key, value in data.items()
                    ]
        ).as_string(self.db.cursor)))

        data.update({"id": _id})
        self.logger.info(self.db.cursor.mogrify(query, data))
        self.db.cursor.execute(query, data)
        self.db.connection.commit()
        fetch = self.db.cursor.fetchone()
        if fetch is None:
            return 0
        return fetch["id"]
