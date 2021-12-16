from django.contrib import admin
from .models import CarInsurancepayment,PersonalInsurancepayment,Houseinsurancepayment,TravelInsurancepayment
# Register your models here.
admin.site.register(CarInsurancepayment)
admin.site.register(PersonalInsurancepayment)
admin.site.register(Houseinsurancepayment)
admin.site.register(TravelInsurancepayment)