from rest_framework import serializers
from .models import Phonebill,Electricitybill,Internetbill,Waterbill


class Phoneserializer(serializers.ModelSerializer):
    class Meta:
        model=Phonebill
        fields='__all__'

class Waterserializer(serializers.ModelSerializer):
    class Meta:
        model=Waterbill
        fields='__all__'

class Internetserializer(serializers.ModelSerializer):
    class Meta:
        model=Internetbill
        fields='__all__'

class Electricityserializer(serializers.ModelSerializer):
    class Meta:
        model=Electricitybill
        fields='__all__'