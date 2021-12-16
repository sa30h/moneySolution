from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Merchant(models.Model):
    user    =   models.OneToOneField("authentication.User",on_delete=models.CASCADE)
    collected_amount=models.IntegerField()
    merchant_name= models.CharField(max_length=100)