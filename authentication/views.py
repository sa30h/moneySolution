from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate,login,get_user_model,logout
from rest_framework import generics,status
from rest_framework.response import Response
from .models import *
from .serializer import OtpVerificationSerializer,RegisterSerializer,LoginSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# from django.contrib.auth import get_user_model
# Create your views here.

#hmac
# import requests
import hmac
import hashlib
from random import randrange
from hashlib import blake2b
import json


class RegisterApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class LoginWithTokenAuthenticationAPIView(GenericAPIView):
    queryset= User.objects.all()
    serializer_class    =       LoginSerializer
    permission_classes     =   []
    authentication_classes =   []

    def post(self,request):
        username    =   request.data.get('username')
        password    =   request.data.get('password')
        print('username',username)
        print('password',password)
        # user        =   User.objects.get(email=str(email))
        user          =   authenticate(username=username,password=password)
        print(user)
        if user is not None:
            # login(user,request)
            #TOKEN STUFF
            token, _ = Token.objects.get_or_create(user = user)
            login(request,user)
            #token_expire_handler will check, if the token is expired it will generate new one
            # is_expired, token = token_expire_handler(token)     # The implementation will be described further

            return Response({ 
                'token': token.key,
                'id':user.id,
            } )
        response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response)

class OtpGeneratorAPIView(generics.GenericAPIView):
	serializer_class 	=	OtpVerificationSerializer

	def post(self,request):
		mobile_number 	=	request.data['mobile_number']
		otp 			=    randrange(1000,9999)
		try:
			OtpVerification.objects.get_or_create(mobile_number=mobile_number,otp=otp)
			msg = str(otp) + " is your  OTP."
			# BASE_URL 	= "https://sms.arkesel.com/sms/api?action=send-sms&api_key=Om83TTlZT2FvUUtqV0s4M0Y=&to="+mobile_number+F"&from=HDPlus&sms="+msg
			# print(BASE_URL)
			# res 	=	requests.get(BASE_URL)
			# print(res.json())
			response 	=	{
				"mobile_number":mobile_number,
				"otp":otp
			}
			return Response(response)
		except:
			data =	OtpVerification.objects.get(mobile_number=mobile_number)
			data.otp 	=	otp
			data.save()
			# msg = str(otp) + " is your  OTP."
			# BASE_URL 	= "https://sms.arkesel.com/sms/api?action=send-sms&api_key=Om83TTlZT2FvUUtqV0s4M0Y=&to="+mobile_number+F"&from=HDPlus&sms="+msg
			# res 	=	requests.get(BASE_URL)
			# print(res.json())
			response 	=	{
				"mobile_number":mobile_number,
				"otp":otp
			}
			return Response(response)


class OtpValidation(generics.GenericAPIView):
	serializer_class 	=	OtpVerificationSerializer

	def post(self,request):
		mobile_number 	=	request.data['mobile_number']
		otp 			=    request.data['otp']
		mobile 			=	 OtpVerification.objects.get(mobile_number=mobile_number)
		print(mobile.otp)
		print(mobile.otp==otp)
		if mobile.otp==otp:
			# username	= 	 request.GET.get('username')
			user 	=	User.objects.get(mobile_number=mobile_number)
			# user.mobile_number = mobile_number
			user.is_verified = True
			user.save()
			response 	=	{
				"status":200,
				"message":"number verified"
			}
			return Response(response)


		response 	=	{
			"status":400,
			"message":"invalid details"
		}
		return Response(response)

