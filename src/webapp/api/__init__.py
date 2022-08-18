from flask import Blueprint
api = Blueprint('api', __name__)

from . import test_api  # noqa
from . import currency_api  # noqa
from . import category_api  # noqa
from . import language_api  # noqa
