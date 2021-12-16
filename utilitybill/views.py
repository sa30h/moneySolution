from django.shortcuts import render
# from rest_framework.generics import GenericApiView
from rest_framework.generics import GenericAPIView
from .models import *
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,ListModelMixin
from .serializer import Phoneserializer,Electricityserializer,Internetserializer,Waterserializer
from utilitybill import serializer
# Create your views here.


class C_PhonebillApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =Phonebill.objects.all()
    serializer_class    =Phoneserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_PhonebillApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =Phonebill.objects.all()
    serializer_class    = Phoneserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


class C_WaterbillApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =Waterbill.objects.all()
    serializer_class    =Waterserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_WaterbillApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =Waterbill.objects.all()
    serializer_class    = Waterserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

class C_InternetbillApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =Internetbill.objects.all()
    serializer_class    =Internetserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_InternetbillApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =Internetbill.objects.all()
    serializer_class    = Internetserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

class C_ElectricitybillApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =Electricitybill.objects.all()
    serializer_class    =Electricityserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_ElectricitybillApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =Electricitybill.objects.all()
    serializer_class    = Electricityserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)




