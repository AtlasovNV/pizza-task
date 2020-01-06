from django.contrib import admin
from .models import ProductPizza, ProductClassics, ProductSpecials, ProductDrinks

admin.site.register(ProductPizza)
admin.site.register(ProductClassics)
admin.site.register(ProductSpecials)
admin.site.register(ProductDrinks)