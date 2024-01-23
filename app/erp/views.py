from django.http import HttpResponse
from django.shortcuts import render

# Create your vistas here.
def Inicio(request):
    return render(request, 'inicio.html')