from .models import Productos, Order, OrderItem, ShippingAdress
import json


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
                    'imagen': product.foto
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