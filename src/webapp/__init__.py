from flask import Flask

from src.db_connect import DBConnect

db = DBConnect()


def create_app(config_filename):
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)
    db.init_app(app)

    from src.webapp.main import main
    app.register_blueprint(main, url_prefix='')

    from src.webapp.api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
