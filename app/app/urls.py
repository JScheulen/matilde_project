"""
URL configuration for app project.

The `urlpatterns` list routes URLs to vistas. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function vistas
    1. Add an import:  from my_app import vistas
    2. Add a URL to urlpatterns:  path('', vistas.home, name='home')
Class-based vistas
    1. Add an import:  from other_app.vistas import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from erp.views import Inicio

from erp.vistas.category.views import tienda, homepage, carrito, checkout

app_name = "gestion"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='inicio'),
    path('tienda/', tienda, name='tienda'),
    path('cart/', carrito, name='carro'),
    path('checkout/', checkout, name='checkout')

]
