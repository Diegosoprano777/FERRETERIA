from rest_framework import serializers
from .models import ProductoPerecedero


class ProductoPerecederoSerializer(serializers.ModelSerializer):
    precio_oferta = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = ProductoPerecedero
        fields = ["id", "nombre", "sku", "precio_regular", "dias_vencimiento", "precio_oferta"]

    def validate_dias_vencimiento(self, value):
        if value < 0:
            raise serializers.ValidationError("Los días para vencer no pueden ser negativos")
        return value

    def validate_precio_regular(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio regular no puede ser negativo")
        return value

