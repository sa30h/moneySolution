from django.db import models
from django.utils import timezone
from authentication.models import User
# Create your models here.

billstatuschoice=[('processing','PROCESSING'),('success','SUCCESS'),('pending','PENDING'),('failed','FAILED')]


class Phonebill(models.Model):
    provider=models.CharField(max_length=100)
    ammount=models.PositiveIntegerField()
    transaction_id=models.CharField(max_length=100)
    paid_by     =models.ForeignKey(User,on_delete=models.CASCADE)
    status  =models.CharField(max_length=100,choices=billstatuschoice)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)

class Electricitybill(models.Model):
    provider=models.CharField(max_length=100)
    ammount=models.PositiveIntegerField()
    transaction_id=models.CharField(max_length=100)
    paid_by     =models.ForeignKey(User,on_delete=models.CASCADE)
    status  =models.CharField(max_length=100,choices=billstatuschoice)    
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)

class Waterbill(models.Model):
    provider=models.CharField(max_length=100)
    ammount=models.PositiveIntegerField()
    transaction_id=models.CharField(max_length=100)
    paid_by     =models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)
    status  =models.CharField(max_length=100,choices=billstatuschoice)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)

class Internetbill(models.Model):
    provider=models.CharField(max_length=100)
    ammount=models.PositiveIntegerField()
    transaction_id=models.CharField(max_length=100)
    paid_by     =models.ForeignKey(User,on_delete=models.CASCADE)
    status  =models.CharField(max_length=100,choices=billstatuschoice)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
