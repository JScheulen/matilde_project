from django.shortcuts import render, redirect, HttpResponseRedirect
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
    success_url = reverse_lazy('iniciar')

    #def post(self, request, *args, **kwargs):
        #print(request.POST)
        #form = ProductosForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return HttpResponseRedirect(self.success_url)
        #return render(request, self.template_name, {'form': form})



