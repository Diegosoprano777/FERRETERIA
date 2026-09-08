from django.test import TestCase
from django.core.exceptions import ValidationError
from modulo_inventario.models import Producto

class ProductoModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Martillo",
            codigo="M123",
            precio_base=10000.00,
            stock=10
        )
    def test_calcular_precio_con_iva(self):
        precio_esperado = 10000.00 * 1.19
        self.assertEqual(self.producto.calcular_precio_con_iva(), round(precio_esperado, 2))

    def test_validaciomn_stock_negativo(self):
        self.producto.stock = -5
        with self.assertRaises(ValidationError):
            self.producto.clean()
            