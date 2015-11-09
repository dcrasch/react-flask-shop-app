from flask_admin.contrib import sqla
from flask_admin.model.form import InlineFormAdmin
from .models import Product, ProductVariant

class ProductVariantInline(InlineFormAdmin):
    pass

class ProductAdmin(sqla.ModelView):
    inline_models = (ProductVariantInline(ProductVariant),)
