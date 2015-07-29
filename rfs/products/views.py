import logging

from flask import Blueprint, render_template

from rfs.products.models import Product
from rfs.app import db

logger = logging.getLogger(__name__)

products = Blueprint('products', __name__, static_folder='static',url_prefix='/products')

@products.route('/')
def index():
    return render_template("index.html")
