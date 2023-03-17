import click
from sqlalchemy.orm.mapper import configure_mappers
from flask.cli import with_appcontext

from rfs.extensions import db
from rfs.products.models import Product, ProductVariant
from rfs.orders.models import Order,OrderLine

@click.command("initdb")
@with_appcontext
def initdb():
    """ Create example data."""
    db.drop_all()
    configure_mappers()
    db.create_all()
    
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

    print("Created database with sample data")
