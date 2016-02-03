import enum
from sqlalchemy_utils import ChoiceType

from rfs.app import db
from rfs.products.models import ProductVariant

    
class Order(db.Model):
    __tablename__ = 'orders'
    TYPES = [(10,'Cart'),
             (20,'Checkout'),
             (30,'Confirmed'),
             (40,'Paid'),
             (50,'Completed')]
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    ordertype = db.Column(ChoiceType(TYPES))

class OrderItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    productvariant_id = db.Column(db.Integer, db.ForeignKey('productvariants.id'))
    productvariant =  db.relationship("ProductVariant")

    quantity = db.Column(db.Integer)
    data = db.Column(db.String(1024), nullable=False)
                         
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship("Order", backref=db.backref('orderlines', order_by=id)) 
