import logging
import uuid
from flask import Blueprint, render_template, current_app, session, jsonify

from rfs.app import db
from rfs.cart.models import Cart

logger = logging.getLogger(__name__)

cart = Blueprint('cart', __name__, static_folder='static',url_prefix='/cart')

@cart.route('/')
def index():
    cart_id = session.get('cart_id',None)
    if cart_id is None:
        cart = Cart()
        cart.token = uuid.uuid4().hex
        db.session.add(cart)
        db.session.commit()
        cart_id=cart.id
        session['cart_id']=cart_id
    else:        
        cart = Cart.query.get(cart_id)
    cart_data = {'id': cart.id,
                 'token': cart.token,
                 'item_count':0,
                 'items':[]
                 }
    
    current_app.logger.debug('Shopping cart')
    return jsonify(cart_data)

@cart.route('remove')
def remove():
    current_app.logger.debug('Shopping cart remove')
    return render_template('index.html')
