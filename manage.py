# -*- coding: utf-8 -*-
import sys
import os

from flask import url_for
from flask.ext.script import Manager
from rfs.app import create_app

app = create_app(config=os.environ.get('APP_CONFIG', 'rfs.config.DevelopmentConfig'))
manager = Manager(app)

@manager.command
def create_all():
    from rfs.app import db
    db.create_all()

@manager.command
def create_data():
    from rfs.app import db
    from rfs.products.models import Product, ProductVariant
    from rfs.orders.models import Order,OrderLine
    
    product = Product()
    product.title = "Product 1"
    product.description = "Product 1 description"

    productvariant = ProductVariant()
    productvariant.title="ProductVariant 1"
    productvariant.description="ProductVariant 1 description"
    productvariant.price = 100
    productvariant.sku = "sku 1"
    productvariant.inventory= 10
    productvariant.mainproduct=product
    
    order = Order()
    order.id=1
    order.ordertype=10
    order.title ='Shopping basket'

    orderline = OrderLine()
    orderline.productvariant=productvariant
    orderline.quantity=1
    orderline.unit_price=100
    orderline.extradata="test orderline"
    orderline.order=order
    
    db.session.add(order)
    db.session.commit()


@manager.command
def run():
    """
    Run the application.  If the environment variable `APP_CONFIG` is not set,
    then the default development config `flaskplate.config.DevelopmentConfig`
    will be used.
    To set the path to a different development config:
        export APP_CONFIG=python.path.to.my.ConfigClass
        python manage.py run
    """
    app.run()

@manager.command
def assets():
    from flask.ext.assets import ManageAssets
    from rfs.app import assets
    ManageAssets(assets)

@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)
    
if __name__ == "__main__":
    manager.run()
