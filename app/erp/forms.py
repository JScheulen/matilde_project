from django.forms import ModelForm, TextInput, Textarea

from erp.models import Productos


class ProductosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Productos
        fields = '__all__'
        # exclude =
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Nombre',

                }

            ),
            'codigo': TextInput(
                attrs={
                    'placeholder': 'Ingrese codigo de producto',

                }

            ),
            'cantidad': TextInput(
                attrs={
                    'placeholder': 'Ingrese',

                }

            ),
            'precio': TextInput(
                attrs={
                    'placeholder': 'Ingrese',
                }

            ),
            'actividad': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Nombre',
                }

            ),
            'foto': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Nombre',
                }

            )
        }
