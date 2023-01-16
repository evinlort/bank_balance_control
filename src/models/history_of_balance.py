from psycopg2 import sql

from src.models.base_model import BaseModel


class HistoryOfBalance(BaseModel):
    @staticmethod
    def get_table():
        return "history_of_balances"
