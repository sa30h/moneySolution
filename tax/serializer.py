from rest_framework import serializers
from .models import Taxpayment


class Taxserializer(serializers.ModelSerializer):
    class Meta:
        model=Taxpayment
        fields='__all__'

