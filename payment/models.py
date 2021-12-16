from django.db import models
from authentication.models import User
from django.db.models.signals import pre_save

# we have to add stripe key for create stripeId
# Create your models here.
class BillingProfile(models.Model):
    user                =       models.OneToOneField(User,on_delete=models.CASCADE)
    email               =       models.EmailField(unique=True)
    active              =       models.BooleanField(default=True)
    stripe_id           =       models.CharField(max_length=120,null=True,blank=True)
    timestamp           =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)
    ammount             =       models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    total_ammount             =       models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    links       =       models.SlugField(blank=True,default=" ")



    def __str__(self):
        return self.email


def user_created_receiver(instance,sender,created,*args,**kwargs):
    if created:
        account = stripe.Account.create(
                      type="express",
                      country="US",
                      email=instance.email,
                      capabilities={
                        "card_payments": {"requested": True},
                        "transfers": {"requested": True},
                      },
                      
                    )
        print('accoutn',account)
        # sa30
        account_links = stripe.AccountLink.create(
        account= account.id,
        refresh_url='https://stripe.com',
        return_url='https://stripe.com',
        type='account_onboarding',
        )
        print('account_links',account_links)
        BillingProfile.objects.get_or_create(User=instance,email=instance.email,stripe_id=account.id,links=account_links.url)
        


# post_save.connect(user_created_receiver,sender=User)

    