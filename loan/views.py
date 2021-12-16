from django.shortcuts import render
# from rest_framework.generics import GenericApiView
from rest_framework.generics import GenericAPIView
from .models import *
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin,ListModelMixin
from .serializer import Houseloanserializer,Personalloanserializer,Businessloanserializer
from utilitybill import serializer
# Create your views here.


class C_HouseloanApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =Houseloan.objects.all()
    serializer_class    =Houseloanserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_HouseloanApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =Houseloan.objects.all()
    serializer_class    = Houseloanserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


class C_PersonalloanApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =Personalloan.objects.all()
    serializer_class    =Personalloanserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_PersonalloanApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =Personalloan.objects.all()
    serializer_class    = Personalloanserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

class C_BusinessloanApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =Businessloan.objects.all()
    serializer_class    =Businessloanserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class RUD_BusinessloanApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =Businessloan.objects.all()
    serializer_class    = Businessloanserializer
    lookup_field='id'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

