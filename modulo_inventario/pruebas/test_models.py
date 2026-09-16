from decimal import Decimal
from django.test import TestCase
from django.core.exceptions import ValidationError
from modulo_inventario.models import ProductoPerecedero

class ProductoPerecederoModelTest(TestCase):
    def test_calcular_descuento_automatico_menos_de_5_dias(self):
        producto = ProductoPerecedero.objects.create(
            nombre="Leche Entera 1L",
            sku="LECHE-001",
            precio_regular=Decimal("1000.00"),
            dias_vencimiento=3
        )
        self.assertEqual(producto.precio_oferta, Decimal("800.00"))

    def test_sin_descuento_5_o_mas_dias(self):
        producto = ProductoPerecedero.objects.create(
            nombre="Yogurt Fresa 500g",
            sku="YOGURT-002",
            precio_regular=Decimal("1000.00"),
            dias_vencimiento=7
        )
        self.assertEqual(producto.precio_oferta, Decimal("1000.00"))

    def test_validacion_dias_vencimiento_negativo(self):
        producto = ProductoPerecedero(
            nombre="Queso Crema",
            sku="QUESO-003",
            precio_regular=Decimal("5000.00"),
            dias_vencimiento=-2
        )
        with self.assertRaises(ValidationError):
            producto.full_clean()