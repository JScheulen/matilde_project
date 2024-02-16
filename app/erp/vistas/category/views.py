from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from erp.models import Productos, Order


def homepage(request):
    return render(request, 'home.html')

def tienda(request):
    products = Productos.objects.all()
    context = {'producto': products}
    return render(request, 'tienda.html', context)

def carrito(request):
    if request.user.is_authenticated:
        customer = request.user.costumer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'carro.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.costumer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        items = []

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)

#def updateItem(request):
    #return JsonResponse('Item was Added', safe=False)

