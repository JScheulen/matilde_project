from django import forms

from .models import Productos, Order, OrderItem, ShippingAdress, Costumer
import json
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User



def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    itemsList = order['get_cart_items']
    try:
        for i in cart:
            itemsList += cart[i]["quantity"]
            product = Productos.objects.get(codigo=i)
            total = (float(product.precio) * float(cart[i]["quantity"]))

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product': {
                    'codigo': product.codigo,
                    'nombre': product.nombre,
                    'precio': product.precio,
                    'foto': product.foto
                },
                'quantity': cart[i]['quantity'],
                'get_total': total

            }
            items.append(item)
    except:
        pass
    return {'items': items, 'order': order, 'itemsList': itemsList}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.costumer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        itemsList = order.get_cart_items
        items = order.orderitem_set.all()
    else:
        cookie_data = cookieCart(request)
        items = cookie_data['items']
        order = cookie_data['order']
        itemsList = cookie_data['itemsList']

    return {'items': items, 'order': order, 'itemsList': itemsList}


def gestOrder(request, data):
    name = data['form']['nombre']
    correo = data['form']['correo']
    print(name)
    cookieData = cookieCart(request)
    items = cookieData['items']
    customer, created = Costumer.objects.get_or_create(
        email=correo,
    )
    customer.name = name
    customer.save()
    order = Order.objects.create(customer=customer, complete=False, )

    for item in items:

        product = Productos.objects.get(codigo=item['product']['codigo'])

        orderitem = OrderItem.objects.create(product=product, order=order, quantity=item['quantity'])

    return customer, order

class CreacionUsuario(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Retipa Contraseña'

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de Usuario',
                    'id': 'name_1'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email_1',
                    'placeholder': 'Ingrese Correo'
                }
            ),
        }