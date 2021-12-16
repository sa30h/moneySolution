from django.shortcuts import render
# from rest_framework.generics import GenericApiView
from rest_framework.generics import GenericAPIView
from .models import *
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,ListModelMixin
from .serializer import Carinsuranceserializer,Houseinsuranceserializer,Travelinsuranceserializer,Personalinsuranceserializer
from utilitybill import serializer
# Create your views here.


class C_CarinsuraceApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =CarInsurancepayment.objects.all()
    serializer_class    =Carinsuranceserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_CarinsuranceApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =CarInsurancepayment.objects.all()
    serializer_class    = Carinsuranceserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


class C_HouseinsuranceApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =Houseinsurancepayment.objects.all()
    serializer_class    =Houseinsuranceserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_HouseinsuranceApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =Houseinsurancepayment.objects.all()
    serializer_class    = Houseinsuranceserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

class C_PersonalinsuranceApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =PersonalInsurancepayment.objects.all()
    serializer_class    =Personalinsuranceserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_PersonalinsuranceApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =PersonalInsurancepayment.objects.all()
    serializer_class    = Personalinsuranceserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

class C_TravelinsuranceApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =TravelInsurancepayment.objects.all()
    serializer_class    =Travelinsuranceserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_TravelinsuranceApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =TravelInsurancepayment.objects.all()
    serializer_class    = Travelinsuranceserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)




