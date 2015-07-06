from rfs.app import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(512))

class ProductVariant(db.model)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text)
    sku = db.Column(db.String(512))
    price = db.Column(db.Integer))
    inventory = db.Column(db.Integer))

    mainproduct_id = db.Column(Integer, ForeignKey('products.id'))
    mainproduct = relationship("Product", backref=backref('varients', order_by=id))
