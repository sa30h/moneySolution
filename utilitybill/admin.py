from django.contrib import admin
from .models import Phonebill,Electricitybill,Waterbill,Internetbill
# Register your models here.
admin.site.register(Phonebill)
admin.site.register(Electricitybill)
admin.site.register(Waterbill)
admin.site.register(Internetbill)
