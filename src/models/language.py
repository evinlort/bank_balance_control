from src.models.base_model import BaseModel


class Language(BaseModel):
    @staticmethod
    def get_table():
        return "languages"
