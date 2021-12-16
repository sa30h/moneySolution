from django.db import models
from django.utils import timezone
from authentication.models import User
# Create your models here.

billstatuschoice=[('processing','PROCESSING'),('success','SUCCESS'),('pending','PENDING'),('failed','FAILED')]
intallmentchoice=[('onetime','ONETIME'),('daily','DAILY'),('weekly','WEEKLY'),('monthly','MONTHLY'),('yearly','YEARLY')]

class Personalloan(models.Model):
    provider=models.CharField(max_length=100)
    ammount=models.PositiveIntegerField()
    installment=models.CharField( max_length=50,choices=intallmentchoice)
    transaction_id=models.CharField(max_length=100)
    paid_by     =models.ForeignKey(User,on_delete=models.CASCADE)
    status  =models.CharField(max_length=100,choices=billstatuschoice)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)

class Businessloan(models.Model):
    provider=models.CharField(max_length=100)
    ammount=models.PositiveIntegerField()
    installment=models.CharField( max_length=50,choices=intallmentchoice)
    transaction_id=models.CharField(max_length=100)
    paid_by     =models.ForeignKey(User,on_delete=models.CASCADE)
    status  =models.CharField(max_length=100,choices=billstatuschoice)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)

class Houseloan(models.Model):
    provider=models.CharField(max_length=100)
    ammount=models.PositiveIntegerField()
    installment=models.CharField( max_length=50,choices=intallmentchoice)
    transaction_id=models.CharField(max_length=100)
    paid_by     =models.ForeignKey(User,on_delete=models.CASCADE)
    status  =models.CharField(max_length=100,choices=billstatuschoice)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)


    
