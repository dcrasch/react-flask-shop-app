from rfs.app import db

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(128))
    # account
    
class CartLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    productvariant_id = db.Column(db.Integer, db.ForeignKey('productvariants.id'))
    productvariant =  db.relationship("ProductVariant")

    quantity = db.Column(db.Integer)
    data = db.Column(db.String(2048), nullable=False)
                         
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    cart = db.relationship("Cart", backref=db.backref('cartlines', order_by=id))
