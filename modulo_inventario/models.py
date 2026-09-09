from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError

class ProductoPerecedero(models.Model):
    nombre = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    precio_regular = models.DecimalField(max_digits=10, decimal_places=2)
    dias_vencimiento = models.IntegerField()
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def clean(self):
        if self.dias_vencimiento is not None and self.dias_vencimiento < 0:
            raise ValidationError("Los días para vencer no pueden ser negativos")
        if self.precio_regular is not None and self.precio_regular < 0:
            raise ValidationError("El precio regular no puede ser negativo")

    def calcular_precio_oferta(self):
        if self.precio_regular is None:
            return None
        if self.dias_vencimiento is not None and self.dias_vencimiento < 5:
            return round(Decimal(str(self.precio_regular)) * Decimal('0.80'), 2)
        return round(Decimal(str(self.precio_regular)), 2)

    def save(self, *args, **kwargs):
        self.clean()
        self.precio_oferta = self.calcular_precio_oferta()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.sku})"