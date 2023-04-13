from .serializers import AccountSerializers, PostSerializers, DoktorSerializers, BulimSerializers
from rest_framework import viewsets
from .models import Account, Post, Bulim, Doktor
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AccountView(viewsets.ModelViewSet):
    serializer_class = AccountSerializers
    queryset = Account.objects.all()

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

class DoktorView(viewsets.ModelViewSet):
    serializer_class = DoktorSerializers
    queryset = Doktor.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

class BulimView(viewsets.ModelViewSet):
    serializer_class = BulimSerializers
    queryset = Bulim.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]