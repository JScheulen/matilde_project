from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):
    codigo = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255, unique=True)
    cantidad = models.IntegerField(default=1)
    precio = models.DecimalField(default=0.00, decimal_places=2, max_digits=9)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Costumer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum(item.quantity for item in orderitems)
        return total

    def __str__(self):
        return str(self.transaction_id)

class OrderItem(models.Model):
    product = models.ForeignKey(Productos, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.precio * self.quantity
        return total

    def __str__(self):
        return self.product.nombre


class ShippingAdress(models.Model):
    customer = models.ForeignKey(Costumer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    ciudad = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.address

