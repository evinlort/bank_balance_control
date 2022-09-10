from src.models.base_model import BaseModel


class Purchase(BaseModel):
    @staticmethod
    def get_table():
        return "purchases"
