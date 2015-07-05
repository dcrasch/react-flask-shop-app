import logging
from flask import Blueprint, render_template, current_app

logger = logging.getLogger(__name__)

products = Blueprint('products', __name__)

@products.route('/')
def index():
    current_app.logger.debug('Do things here')
    return render_template('index.html')
