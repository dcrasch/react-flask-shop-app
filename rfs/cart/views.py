import logging
import uuid
from flask import Blueprint, render_template, current_app, session, jsonify, request

from rfs.app import db
from rfs.cart.models import Cart, CartLine

logger = logging.getLogger(__name__)

cart = Blueprint('cart', __name__, static_folder='static',url_prefix='/cart')

@cart.route('/')
def getCart():
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

    cart_data = {"token": cart.token,
                 "items": [{"id":i.productvariant.mainproduct.id,
                            "title":i.productvariant.mainproduct.title,
                            "description":i.productvariant.mainproduct.description,
                            "image": i.productvariant.mainproduct.image,                          
                            "variant_id" : i.productvariant.id,
                            "variant_title" : i.productvariant.title,
                            "variant_description": i.productvariant.description,
                            "variant_sku" : i.productvariant.sku,
                            "variant_price": i.productvariant.price,

                            "line_price" : i.quantity * i.productvariant.price,
                            "price" : i.productvariant.price,
                            "quantity" :i.quantity
                            } for i in cart.cartlines],
                 "total_price" : sum([currentline.quantity*i.productvariant.price for i in cart.cartlines]),
                 "item_count" : len(cart.cartlines)
                 }

    current_app.logger.debug('Shopping cart')
    return jsonify(cart_data)

@cart.route('/add', methods=['POST'])
def addItem():
    quantity = request.form['quantity']
    productvariant_id = request.form['id']

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

    currentline = None
    for i in cart.cartlines:
        if i.productvariant_id == productvariant_id:
            currentline = i
            currentline.quantity+=1
            break
    if not currentline:
        currentline = CartLine()
        currentline.productvariant_id = productvariant_id
        currentline.quantity = 1
        currentline.cart_id = cart.id
        currentline.data=""
        db.session.add(currentline)
        db.session.commit()
        
    #add to cartline
    cartline_data = {"id":currentline.productvariant.mainproduct.id,
                        "title":currentline.productvariant.mainproduct.title,
                        "description":currentline.productvariant.mainproduct.description,
                            "image": currentline.productvariant.mainproduct.image,                          
                            "variant_id" : currentline.productvariant.id,
                            "variant_title" : currentline.productvariant.title,
                            "variant_description": currentline.productvariant.description,
                            "variant_sku" : currentline.productvariant.sku,
                            "variant_price": currentline.productvariant.price,

                            "line_price" : currentline.quantity* currentline.productvariant.price,
                            "price" : currentline.productvariant.price,
                            "quantity" :currentline.quantity
                            }
    current_app.logger.debug('Shopping cartline')
    return jsonify(cartline_data)

@cart.route('/change' ,methods=['POST'])
def changeItem():
    quantity = request.form['quantity']
    productvariant_id = request.form['id']

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

    for i in cart.cartlines:
        if i.productvariant_id == productvariant_id:
            if quantity==0:
                session.delete(i)
                session.commit()
            else:
                i.quantity = quantity
                session.update(i)
                session.commit()
    cart_data = {"token": cart.token,
                 "items": [{"id":i.productvariant.mainproduct.id,
                            "title":i.productvariant.mainproduct.title,
                            "description":i.productvariant.mainproduct.description,
                            "image": i.productvariant.mainproduct.image,                          
                            "variant_id" : i.productvariant.id,
                            "variant_title" : i.productvariant.title,
                            "variant_description": i.productvariant.description,
                            "variant_sku" : i.productvariant.sku,
                            "variant_price": i.productvariant.price,

                            "line_price" : i.quantity * i.productvariant.price,
                            "price" : i.productvariant.price,
                            "quantity" :i.quantity
                            } for i in cart.cartlines],
                 "total_price" : sum([i.productvariant.price*i.productvariant.quantity for i in cart.cartlines]),
                 "item_count" : len(cart.cartlines)
                 }

    current_app.logger.debug('Shopping remove item')
    return jsonify(cart_data)

@cart.route("clear")
def clear():
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

        for i in cart.cartlines:
            session.delete(i)
            session.commit()
            
     cart_data = {"token": cart.token,
                 "items": [{"id":i.productvariant.mainproduct.id,
                            "title":i.productvariant.mainproduct.title,
                            "description":i.productvariant.mainproduct.description,
                            "image": i.productvariant.mainproduct.image,                          
                            "variant_id" : i.productvariant.id,
                            "variant_title" : i.productvariant.title,
                            "variant_description": i.productvariant.description,
                            "variant_sku" : i.productvariant.sku,
                            "variant_price": i.productvariant.price,

                            "line_price" : i.quantity * i.productvariant.price,
                            "price" : i.productvariant.price,
                            "quantity" :i.quantity
                            } for i in cart.cartlines],
                 "total_price" : sum([currentline.quantity*i.productvariant.price for i in cart.cartlines]),
                 "item_count" : len(cart.cartlines)
                 }

    current_app.logger.debug('Shopping remove item')
    return jsonify(cart_data)
