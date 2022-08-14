from src.models.base_model import BaseModel


class Currency(BaseModel):
    @staticmethod
    def get_table():
        return "currencies"
