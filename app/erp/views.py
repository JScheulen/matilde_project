from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from erp.models import Productos


# Create your vistas here.
def Inicio(request):
    data = {
        'categories': Productos.objects.all()
    }
    return render(request, 'inicio.html', data)


