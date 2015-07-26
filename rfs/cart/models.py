from rfs.app import db
from rfs.app.products.model import Products

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    # account
    
class CartLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product =  db.relationship("Product")

    quantity = db.Column(db.Integer)
    data = db.Column(db.String(1024), nullable=False)
                         
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    cart = db.relationship("Cart", backref=db.backref('cartlines', order_by=id))
