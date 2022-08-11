from src.webapp import db


class BaseModel:
    def __init__(self, dbp=None):
        if dbp:
            self.db = dbp
        else:
            self.db = db

    @staticmethod
    def convert_to_dicts_in_list(fetch_list):
        resulting_list = []
        for fetch_dict in fetch_list:
            resulting_list.append(dict(fetch_dict))
        return resulting_list
