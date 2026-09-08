from django.db import models
from django.core.exceptions import ValidationError

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.TextField(max_length=50, unique=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def clean(self):
        if self.stock < 0:
            raise ValidationError("El precio base no puede ser negativo")

    def calcular_precio_con_iva(self):

        return round(float(self.precio_base) * 1.19, 2)
    


    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
    