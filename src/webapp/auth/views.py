import hashlib

from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, logout_user, login_user

from src.models import User
from src.config import logger
from . import auth


@auth.route('/login', methods=["GET"])
def login():
    return render_template("auth/login.html")


@auth.route('/login', methods=["POST"])
def login_user_to_app():
    username = request.form.get("username")
    password = request.form.get("password")
    hash_password = hashlib.sha1(password.encode("utf-8")).hexdigest()
    u = User()
    u.get_user_for_login(username, hash_password)
    if u and hasattr(u, "id"):
        login_user(u, remember=True, fresh=False)
        return jsonify(True)
    return jsonify(False)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for('auth.login'))
