from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework import views

from core.models.demmand import Demmand
from core.models.address import Address
from api.serializers import UserSerializer, DemmandSerializer, AddressSerializer
from api.permissions import IsOwnerOrReadOnly




class DemmandList(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    queryset = Demmand.objects.all()
    serializer_class = DemmandSerializer

    def perform_create(self, serializer):
        serializer.save(announcer=self.request.user)


class DemmandDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Demmand.objects.all()
    serializer_class = DemmandSerializer


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
