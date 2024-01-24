from django.shortcuts import render
from django.views.generic import ListView

from erp.models import Productos


def producto(request):
    data = {
        'Vistas': Productos.objects.all()
    }
    return render(request, 'inicio.html', data)


class Productos_lista(ListView):
    model = Productos
    template_name = 'inicio.html'
