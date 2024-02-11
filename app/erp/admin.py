from django.contrib import admin

from erp.models import Productos, Costumer, Order, OrderItem, ShippingAdress

#from app.erp.models import *

admin.site.register(Productos)
admin.site.register(Costumer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)


# Register your models here.
