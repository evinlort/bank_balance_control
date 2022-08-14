from src.models.base_model import BaseModel


class Name(BaseModel):
    @staticmethod
    def get_table():
        return "names"
