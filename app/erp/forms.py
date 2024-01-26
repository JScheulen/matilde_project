from django.forms import ModelForm

from erp.models import Productos


class ProductosForm(ModelForm):

    class Meta:
        model = Productos
        fields = '__all__'
        #exclude =
