from src.db_connect import DBConnect
from src.models.user import User


if __name__ == "__main__":
    db = DBConnect()
    db.cursor.execute("select * from languages")
    user = User(db)
    print(user.fetch_by_username("evinlorth"))
