from flask import Blueprint
auth = Blueprint('auth', __name__)
from . import views  # noqa
from . import new_user