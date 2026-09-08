from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CustomObtainAuthToken

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', CustomObtainAuthToken.as_view(), name='custom_obtain_auth_token'),
]
