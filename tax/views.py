from django.db.models import query
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,ListModelMixin
from .serializer import Taxserializer
from .models import Taxpayment
# Create your views here.
class C_TaxpaymentView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Taxpayment.objects.all()
    serializer_class=Taxserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
class RUD_TaxpaymentView(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
    queryset=Taxpayment.objects.all()
    serializer_class=Taxserializer
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.delete(request,*args, **kwargs)