from django.db.models import fields
from rest_framework import serializers
from .models import *



class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        # fields='__all__'
        fields=['username','email','mobile_number','role','address','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        user=User(
            # email=self.validated_data['email'],
            username=self.validated_data['username'],


        )
        password=self.validated_data['password']
        address=self.validated_data['address']
        mobile_number=self.validated_data['mobile_number']
        email=self.validated_data['email']
        role=self.validated_data['role']


        # mobile_number=self.validated_data['mobile_number']
        # mobile=OtpVerification.objects.get()
        # if password !=password2:
        #     raise serializers.ValidationError({'password':"passoword must match"})
        user.address=address
        user.mobile_number=mobile_number
        user.email=email
        user.role=role
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    # email=serializers.EmailField(max_length=50)
    username=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=40)

class OtpVerificationSerializer(serializers.ModelSerializer):
	class Meta:
		model   =   OtpVerification
		fields	=	"__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"