from django.shortcuts import render
from rest_framework import generics
from nrb_data_api.serializers import BioDataSerializer,AddressSerializer
from nrb_data_api.models import BioData,Address

# Biodata
class BioDataList(generics.ListCreateAPIView):
    queryset=BioData.objects.all()
    serializer_class=BioDataSerializer


class BioDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=BioData.objects.all()
    serializer_class=BioDataSerializer

# Biodata
class AddressList(generics.ListCreateAPIView):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer
