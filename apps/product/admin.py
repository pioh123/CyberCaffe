from django.contrib import admin
from .models import Product, Advertise, Promotion

# Register your models here.

admin.site.register(Product)
admin.site.register(Advertise)
admin.site.register(Promotion)