from src.webapp import db


class BaseModel:
    def __init__(self, dbp=None):
        if dbp:
            self.db = dbp
        else:
            self.db = db
