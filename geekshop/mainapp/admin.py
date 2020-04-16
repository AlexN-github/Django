from django.contrib import admin

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Basket)
