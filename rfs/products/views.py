import logging

from flask import Blueprint, render_template, current_app, jsonify, session

from rfs.products.models import Product
from rfs.app import db

logger = logging.getLogger(__name__)

products = Blueprint('products', __name__, static_folder='static',url_prefix='/products')

#GET /products/<product-handle>.js
#POST /cart/add.js
#GET /cart.js
#POST /cart/update.js
#POST /cart/change.js
#POST /cart/clear.js
#GET /cart/shipping_rates.json
    
@products.route('/')
def index():
    if not session.has_key("cart_id"):
        #create new cart
        cart_id = 1
        session['cart_id'] = 1
    else:
        cart_id = 1

    cart = db.session.query(id=1)
    
    cart_data = {"token": cart.token,
                 "items": [{"id":i.productvariant.mainproduct.id,
                            "title":i.productvarient.mainproduct.title,
                            "description":i.productvarient.mainproduct.description,
                            "image": i.productvarient.mainproduct.image,

                             "variant_id" : i.productvariant.id,
                           "variant_title" : i.productvariant.title,
                           "varient_description", i.productvariant.description,
                           "varient_sku" : i.productvariant.sku,
                           "varient_price": i.produtvariant.price
                           } for i in cart.items],
                 "total_price" : sum([i.productvariant.price for i in cart.items])
                 "item_count" : len(cart.items)
                }
    return jsonify(cart_data)
