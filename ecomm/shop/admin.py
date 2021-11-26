from django.contrib import admin
from .models import Product, Contacts, Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Contacts)
admin.site.register(Order)
