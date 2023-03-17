from sqlalchemy import Column

from ..extensions import db

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(512), nullable=False)
    description = Column(db.Text)
    
    # product_type
    def __unicode__(self):
        return str('<Product {!r}>'.format(self.title))
    
class ProductVariant(db.Model):
    __tablename__ = "productvariants"
    
    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(512), nullable=False)
    description = Column(db.Text)
    sku = Column(db.String(512))
    price = Column(db.Integer)
    inventory = Column(db.Integer)
    position = Column(db.Integer)

    mainproduct_id = Column(db.Integer, db.ForeignKey('products.id'))
    mainproduct = db.relationship("Product", backref=db.backref('variants', order_by=id))

    def __unicode__(self):
        return str('<ProductVariant {!r}>'.format(self.title))

class ProductImage(db.Model):
    __tablename__ = "productimages"
    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(512), nullable=False)
    description = Column(db.Text)    
    image = Column(db.String(512))
    position = Column(db.Integer)
