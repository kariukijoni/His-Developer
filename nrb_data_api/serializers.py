from rest_framework import serializers
from.models import Address,BioData

# Biodata
class BioDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=BioData
        fields='__all__'
        

class BioDataDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioData
        fields = '__all__'
        depth = 1


# Address
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'


class AddressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'