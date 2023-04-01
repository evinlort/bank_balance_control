from flask import Blueprint
main = Blueprint('main', __name__)
from .views import (  # noqa
    home,
    test,
    category,
    purchase,
)
