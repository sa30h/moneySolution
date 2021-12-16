from rest_framework import serializers
from .models import CarInsurancepayment,PersonalInsurancepayment,TravelInsurancepayment,Houseinsurancepayment


class Carinsuranceserializer(serializers.ModelSerializer):
    class Meta:
        model=CarInsurancepayment
        fields='__all__'

class Personalinsuranceserializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalInsurancepayment
        fields='__all__'

class Travelinsuranceserializer(serializers.ModelSerializer):
    class Meta:
        model=TravelInsurancepayment
        fields='__all__'

class Houseinsuranceserializer(serializers.ModelSerializer):
    class Meta:
        model=Houseinsurancepayment
        fields='__all__'