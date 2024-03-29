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

from erp.vistas.category.views import tienda, homepage, carrito, checkout, updateItem, processOrder, vista_Item, page_not_found_404, register_user, login_user
from django.conf.urls import handler404

from django.conf.urls.static import static
from django.conf import settings


handler404 = page_not_found_404

app_name = "gestion"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='inicio'),
    path('tienda/', tienda, name='tienda'),
    path('cart/', carrito, name='carro'),
    path('checkout/', checkout, name='checkout'),
    path('registro/', register_user, name='registrar'),
    path('login/', login_user, name='conectar'),
    #Processos de Request Post
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    path('tienda/<str:codigo>/', vista_Item, name='vistas')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


