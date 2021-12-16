from rest_framework import serializers
from .models import Houseloan,Businessloan,Personalloan


class Houseloanserializer(serializers.ModelSerializer):
    class Meta:
        model=Houseloan
        fields='__all__'

class Personalloanserializer(serializers.ModelSerializer):
    class Meta:
        model=Personalloan
        fields='__all__'

class Businessloanserializer(serializers.ModelSerializer):
    class Meta:
        model=Businessloan
        fields='__all__'

