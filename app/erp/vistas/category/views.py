from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from erp.models import Productos, Order, OrderItem, ShippingAdress
import json
import datetime


def homepage(request):
    if request.user.is_authenticated:
        customer = request.user.costumer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

    context = {'order': order}

    return render(request, 'home.html', context)

def tienda(request):
    if request.user.is_authenticated:
        customer = request.user.costumer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

    products = Productos.objects.all()
    context = {'producto': products, 'order': order}
    return render(request, 'tienda.html', context)

def carrito(request):
    if request.user.is_authenticated:
        customer = request.user.costumer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        itemsList = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}

        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        itemsList = order['get_cart_items']

        for i in cart:
            itemsList += cart[i]["quantity"]
            product = Productos.objects.get(codigo=i)
            total = (float(product.precio) * float(cart[i]["quantity"]))

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

    context = {'items': items, 'order': order, 'itemsList': itemsList}
    return render(request, 'carro.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.costumer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()

    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        items = []


    context = {'items': items, 'order': order}

    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productName']
    action = data['action']


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

def encabezado(request):
    if request.user.is_authenticated:
        customer = request.user.costumer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cuenta = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cuenta = order['get_cart_items']

    context = {'items': items, 'order': order, 'cuenta': cuenta}

    return render(request, context)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.costumer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
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

    else:
        print('user is not logged in')

    return JsonResponse('Payment Complete', safe=False)


