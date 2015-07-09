from rfs.app import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(512))

class ProductVariant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text)
    sku = db.Column(db.String(512))
    price = db.Column(db.Integer)
    inventory = db.Column(db.Integer)

    mainproduct_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    mainproduct = db.relationship("Product", backref=db.backref('varients', order_by=id))
