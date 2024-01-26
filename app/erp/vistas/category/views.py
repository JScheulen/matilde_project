from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from erp.models import Productos

from erp.forms import ProductosForm


def producto(request):
    data = {
        'Vistas': Productos.objects.all()
    }
    return render(request, 'inicio.html', data)


class Productos_lista(ListView):
    model = Productos
    template_name = 'inicio.html'

class Productos_CreateView(CreateView):
    model = Productos
    form_class = ProductosForm
    template_name = 'productos.html'


