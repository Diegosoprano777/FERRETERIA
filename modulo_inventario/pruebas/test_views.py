from decimal import Decimal
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from modulo_inventario.models import ProductoPerecedero

class ProductoPerecederoAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        self.producto = ProductoPerecedero.objects.create(
            nombre="Leche Entera 1L",
            sku="LECHE-001",
            precio_regular=Decimal("3500.00"),
            dias_vencimiento=3
        )
        self.url_list = '/api/v1/productos/'
        self.url_detail = f'/api/v1/productos/{self.producto.id}/'

    def test_obtener_productos_retorna_200(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_producto_sin_token_retorna_401(self):
        data = {
            "nombre": "Jamon de Pavo 250g",
            "sku": "JAMON-002",
            "precio_regular": 8500.00,
            "dias_vencimiento": 10
        }
        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_crear_producto_con_token_retorna_201(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            "nombre": "Jamon de Pavo 250g",
            "sku": "JAMON-002",
            "precio_regular": 8500.00,
            "dias_vencimiento": 2
        }
        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductoPerecedero.objects.count(), 2)
        self.assertEqual(response.data["precio_oferta"], "6800.00")

    def test_crear_producto_datos_invalidos_retorna_400(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            "nombre": "Queso Tajado 200g",
            "sku": "QUESO-004",
            "precio_regular": 6000.00,
            "dias_vencimiento": -5
        }
        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)