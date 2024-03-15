from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from erp.models import Productos, Order, OrderItem, ShippingAdress, Costumer
from erp.utils import cookieCart, cartData, gestOrder, CreacionUsuario
import json
import datetime
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    cookieData = cartData(request)
    order = cookieData['order']
    items = cookieData['items']
    itemsList = cookieData['itemsList']
    products = Productos.objects.all()
    context = {'items': items,'order': order, 'itemsList': itemsList, 'producto': products}

    return render(request, 'home.html', context)


def tienda(request):
    cookieData = cartData(request)
    order = cookieData['order']
    items = cookieData['items']
    itemsList = cookieData['itemsList']

    products = Productos.objects.all()
    context = {'producto': products, 'order': order, 'itemsList': itemsList, 'items': items}
    return render(request, 'tienda.html', context)


def carrito(request):
    cookieData = cartData(request)
    items = cookieData['items']
    order = cookieData['order']
    itemsList = cookieData['itemsList']

    context = {'items': items, 'order': order, 'itemsList': itemsList}
    return render(request, 'carro.html', context)


def checkout(request):
    cookieData = cartData(request)
    items = cookieData['items']
    order = cookieData['order']
    itemsList = cookieData['itemsList']

    context = {'items': items, 'order': order, 'itemsList': itemsList}

    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productName']
    action = data['action']

    if action == 'add' or action == 'remove':
        customer = request.user.costumer
        product = Productos.objects.get(codigo=productId)

        order, create = Order.objects.get_or_create(customer=customer, complete=False)

        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)

        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

    return JsonResponse('Item was Added', safe=False)


def vista_Item(request, codigo):

    codigo = Productos.objects.get(codigo=codigo)
    context = {'producto': codigo}


    return render(request, 'detalle_producto.html', context)



def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.costumer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)


    else:
        print('user is not logged in')
        customer, order = gestOrder(request, data)


    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()
    shipping = data['proceso']
    if shipping == 'True':
        ShippingAdress.objects.get_or_create(
            customer=customer,
            order=order,
            address=data['shipping']['direccion'],
            ciudad=data['shipping']['ciudad'],
            codigo_postal=data['shipping']['codigopostal']

        )

    return JsonResponse('Payment Complete', safe=False)

def page_not_found_404(request, exception):
    return render(request, '404.html')

def login_user(request):
    return render(request, 'loggeo.html')

def register_user(request):


    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/tienda")
    else:
        form = UserCreationForm()


    context = {
        "crear": form
    }
    return render(request, 'registro.html', context)
