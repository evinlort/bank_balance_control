from flask import jsonify

from . import api

from src.models import (
    db, Language
)


@api.route('/languages', methods=["GET"])
def get_all_languages():
    langs = Language(db)
    languages = langs.get_all()
    return jsonify(languages)
