from typing import Text
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
# from utils.models   import  BaseAbstarctModel
from .utils import unique_id_generator,random_string_generator



class User(AbstractUser):
    user_choice=(('owner','OWNER'),('customer','CUSTOMER'),('agent','AGENT'))
    # email           =   models.EmailField(unique=True,blank=True)
    mobile_number        =   models.CharField(max_length=20,blank=True)
    role            =   models.CharField(verbose_name='user role',choices=user_choice,max_length=20,default='CUSTOMER')
    address         =   models.CharField(max_length=200,blank=True)
    is_mobile_verified=models.BooleanField(default=False)
    @property
    def owner(self):
        return self.user



@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)


class OtpVerification(models.Model):
    mobile_number 		=		models.CharField(max_length=120,unique=True,blank=True,null=True)
    otp 				=		models.CharField(max_length=120,blank=True,null=True)
    is_varified         =models.BooleanField(default=False)
    def __str__(self):
        return self.mobile_number


class Profile(models.Model):
    user    =   models.OneToOneField(User,on_delete=models.CASCADE)
    refrence_id=models.CharField(max_length=20,null=True,default=None)
    profile_image=models.ImageField(upload_to="profile_image",blank=True,null=True)


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_create_profile(sender,instance=None,created=False,**kwargs):
    if created:
        Profile.objects.create(user=instance)

def pre_save_Profileref_creator(instance,sender,*args,**kwargs):
    def Letters(*args, **kwargs):
        comp='REF'
        string = str(comp)+str(random_string_generator())
        return str(string)
    if instance.user.role is "agent":
        instance.refrence_id = Letters()


pre_save.connect(pre_save_Profileref_creator,sender=Profile)

 

    






