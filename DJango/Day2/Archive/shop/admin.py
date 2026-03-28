from django.contrib import admin
from .models import Product, MyUser , Customer, Product2, orders
# Register your models here.

admin.site.register(Product)
admin.site.register(MyUser)
admin.site.register(Customer)
admin.site.register(Product2)
admin.site.register(orders)

