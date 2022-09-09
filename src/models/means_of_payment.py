from src.models.base_model import BaseModel


class MeansOfPayment(BaseModel):
    @staticmethod
    def get_table():
        return "means_of_payments"
