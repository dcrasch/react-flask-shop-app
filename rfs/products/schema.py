from flask_marshmallow import Marshmallow
ma = Marshmallow()

class ProductSchema(ma.Schema):
    """
    Schema
    """
    class Meta:
        fields = (
        'id', 
        'title'
        )