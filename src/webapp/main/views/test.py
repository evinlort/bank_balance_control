from flask import render_template
from src.webapp.main import main

from src.models import (
    db, User
)
usermod = User(db)


@main.route('/test/<username>', methods=["GET"])
def test_app_working(username):
    user_data = usermod.fetch_by_username(username)
    return render_template('test/index.html', params=user_data)


@main.route('/', defaults={'u_path': ''})
@main.route('/<path:u_path>', methods=["GET", "POST"])
def get_all_pages_after(u_path):
    return "Nice try, dickhead."
