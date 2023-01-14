from flask import render_template
from flask_login import login_required, current_user

from src.config import logger
from src.models import (
    db, Category
)
from src.webapp.main import main


@main.route('/edit/categories', methods=["GET"])
@login_required
def edit_categories():
    cat = Category(db)
    logger.error(current_user.__dict__)
    categories = cat.get_all_family_categories(family_id=current_user.family_id)
    logger.info(categories)
    params = {"categories": categories}
    return render_template("/category/category.html", params=params)
