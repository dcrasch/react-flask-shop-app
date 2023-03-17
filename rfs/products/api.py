from .models import Product, ProductVariant
from .schema import ProductSchema

def get(limit):
    product = Product.query.filter().all()
    product_schema =  ProductSchema(many=True)
    return product_schema.jsonify(product)
