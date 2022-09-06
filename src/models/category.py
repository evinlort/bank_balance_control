import psycopg2.errors
from psycopg2 import sql

from src.models.name import Name
from src.models.translation import Translation
from src.models.base_model import BaseModel


class Category(BaseModel):
    @staticmethod
    def get_table():
        return "categories"

    def get_all_categories(self, language=1) -> list:
        categories = self.get_all()
        self.logger.info(categories)
        translation_model = Translation(self.db)
        for category in categories:
            self.logger.info(category["name_id"])
            translation = translation_model.get_by_name_id_and_language(
                name_id=category["name_id"], language_id=language
            )
            category["name"] = translation["translation"]
        return categories

    def save(self, row):
        names = Name(self.db)
        name_id = names.save(row)
        row["name_id"] = name_id

        translation_model = Translation(self.db)
        translation_model.save(row)

        query = sql.SQL("INSERT INTO {} "
                        "(name_id, created_by, creation_date) "
                        "VALUES (%(name_id)s, %(created_by)s, %(creation_date)s) "
                        "RETURNING id".format(self.table))
        self.logger.info(self.db.cursor.mogrify(query, row))
        try:
            self.db.cursor.execute(query, row)
            self.db.connection.commit()
        except psycopg2.errors.UniqueViolation:
            self.db.connection.rollback()
            query = sql.SQL("SELECT id FROM {} WHERE name_id = %(name_id)s".format(self.table))
            self.db.cursor.execute(query, row)

        return self.db.cursor.fetchone()[0]
