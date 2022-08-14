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
