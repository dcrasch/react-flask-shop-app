from rfs.app import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)

class OrderItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product =  db.relationship("Product")

    quantity = db.Column(db.Integer)
    data = db.Column(db.String(1024), nullable=False)
                         
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship("Cart", backref=db.backref('orderlines', order_by=id)) 
