import logging
from flask import Blueprint, render_template, current_app, session

logger = logging.getLogger(__name__)

cart = Blueprint('cart', __name__, static_folder='static',url_prefix='/cart')

@cart.route('/')
def index():
    current_app.logger.debug('Shopping cart')
    return render_template('index.html')

@cart.route('remove')
def remove():
    current_app.logger.debug('Shopping cart remove')
    return render_template('index.html')
