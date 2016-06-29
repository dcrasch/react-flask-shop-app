from rfs.app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text)
    # product_type
    def __repr__(self):
        return '<Product {!r}>'.format(self.title)
    
class ProductVariant(db.Model):
    __tablename__ = "productvariants"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text)
    sku = db.Column(db.String(512))
    price = db.Column(db.Integer)
    inventory = db.Column(db.Integer)
    position = db.Column(db.Integer)

    mainproduct_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    mainproduct = db.relationship("Product", backref=db.backref('variants', order_by=id))

    def __repr__(self):
        return '<ProductVariant {!r}>'.format(self.title)

class ProductImage(db.Model):
    __tablename__ = "productimages"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text)    
    image = db.Column(db.String(512))
    position = db.Column(db.Integer)
