from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy

from erp.models import Productos


def homepage(request):
    return render(request, 'home.html')

def tienda(request):
    context = {}
    return render(request, 'tienda.html')

def carrito(request):
    context = {}
    return render(request, 'carro.html')

def checkout(request):
    context = {}
    return render(request, 'checkout.html')



