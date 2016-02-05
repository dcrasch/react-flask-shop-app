import logging
from flask import Blueprint, render_template, current_app
from rfs.orders.models import Order

logger = logging.getLogger(__name__)

orders = Blueprint('orders', __name__, static_folder='static',url_prefix='/orders')

@orders.route('/')
def index():
    current_app.logger.debug('Do things here')
    return render_template('cart.html')
