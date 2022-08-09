import os

from flask import Flask
from flask_login import LoginManager
from flask_session import Session

from src.db_connect import DBConnect

db = DBConnect()
login_manager = LoginManager()


def create_app(config_filename):
    os.environ['FLASK_DEBUG'] = "1"
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='Once there is a way to get back homeward',
        SESSION_TYPE='filesystem'
    )

    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'

    sess = Session()
    sess.init_app(app)

    db.init_app(app)

    from src.webapp.main import main
    app.register_blueprint(main, url_prefix='')

    from src.webapp.auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from src.webapp.api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
