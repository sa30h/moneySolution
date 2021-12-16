from django.shortcuts import render 
from .models import Merchant
from .serializer import MerchantSerializer

from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView

# Create your views here.
class CreateMerchantApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset    =   Merchant.objects.all()
    serializer_class    = MerchantSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RUD_MerchatApiView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset    =   Merchant.objects.all()
    serializer_class    = MerchantSerializer
    lookup_field    = 'merchant_name'

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)