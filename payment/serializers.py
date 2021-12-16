from rest_framework import serializers
from .models import BillingProfile

# class BillingProfileSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model 	=	BillingProfile
# 		fields 	=	"__all__"
class BillingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillingProfile
        # fields='__all__'
        fields 		= "__all__"

class StripeTokenSerializer(serializers.Serializer):
    token     =   serializers.CharField(max_length=120)