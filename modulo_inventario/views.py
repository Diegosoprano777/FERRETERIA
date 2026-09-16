from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import ProductoPerecedero
from .serializers import ProductoPerecederoSerializer

class ProductoPerecederoViewSet(viewsets.ModelViewSet):
    queryset = ProductoPerecedero.objects.all().order_by('id')
    serializer_class = ProductoPerecederoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email}, status=status.HTTP_200_OK)

    