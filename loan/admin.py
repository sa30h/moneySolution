from django.contrib import admin
from .models import Houseloan,Businessloan,Personalloan
# Register your models here.
admin.site.register(Houseloan)
admin.site.register(Businessloan)
admin.site.register(Personalloan)