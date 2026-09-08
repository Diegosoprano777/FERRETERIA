from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from modulo_inventario.models import Producto

class ProductoAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        self.producto = Producto.objects.create(
            nombre="Martillo",
            codigo="M123",
            precio_base=10000.00,
            stock=10
        )
        # Corregido: Uso de variables planas
        self.url_list = '/api/v1/productos/'
        self.url_detail = f'/api/v1/productos/{self.producto.id}/'

    def test_obtener_productos_sin_autenticacion(self):
        # Corregido: Llamada a self.url_list
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_crear_producto_sin_token_retorna_401(self):
        data = {
            "nombre": "Destornillador",
            "codigo": "D456",
            "precio_base": 5000.00,
            "stock": 20
        }
        # Corregido: Llamada a self.url_list
        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Corregido: Indentación ajustada al nivel de la clase
    def test_crear_producto_con_token_exitoso(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            "nombre": "Destornillador",
            "codigo": "D456",
            "precio_base": 5000.00,
            "stock": 20
        }
        # Corregido: Llamada a self.url_list
        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Corregido: Producto con P mayúscula
        self.assertEqual(Producto.objects.count(), 2)

    # Corregido: Indentación ajustada al nivel de la clase
    def test_crear_producto_datos_invalidos_retorna_400(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            "nombre": "Destornillador",
            "codigo": "D456",
            "precio_base": -5000.00,
            "stock": 20
        }
        # Corregido: Llamada a self.url_list
        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)