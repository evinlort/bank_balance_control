from flask import render_template

from . import api

from src.models import (
    db, User
)
usermod = User(db)


@api.route('/test/<username>', methods=["GET"])
def get_all_by_username(username):
    user = User(db)
    user_data = user.fetch_by_username(username)
    print(user_data)
    params = {"params": user_data}
    return render_template('test/index.html', **params)
