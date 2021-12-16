from django.db import models
from django.db.models.fields import PositiveIntegerField
from authentication.models import User
# Create your models here.
class Taxpayment(models.Model):
    paid_by =models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    transaction_id=models.CharField(max_length=100)
    date    =models.DateField(auto_now=True)