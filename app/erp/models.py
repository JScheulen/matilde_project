from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255, unique=True)
    cantidad = models.IntegerField(default=1)
    precio = models.DecimalField(default=0.00, decimal_places=2, max_digits=9)
    actividad = models.CharField(max_length=50)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'nuevo_producto'
