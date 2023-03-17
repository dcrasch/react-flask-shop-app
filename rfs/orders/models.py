from sqlalchemy import Column
from sqlalchemy_utils import ChoiceType

from ..extensions import db

from rfs.products.models import ProductVariant

class Order(db.Model):
    __tablename__ = 'orders'
    TYPES = [(10,'Cart'),
             (20,'Checkout'),
             (30,'Confirmed'),
             (40,'Paid'),
             (50,'Completed')]
    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(512), nullable=False)
    ordertype = Column(db.Integer)

class OrderLine(db.Model):
    id = Column(db.Integer, primary_key=True)

    order_id = Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship("Order", backref=db.backref('orderlines', order_by=id)) 
        
    productvariant_id = Column(db.Integer, db.ForeignKey('productvariants.id'),nullable=True)
    productvariant =  db.relationship("ProductVariant")
        
    quantity = Column(db.Integer)
    unit_price = Column(db.Integer)    
    extradata = Column(db.String(1024), nullable=False)                        
