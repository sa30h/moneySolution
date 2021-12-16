from django.contrib import admin
from .models import User,OtpVerification,Profile
# Register your models here.
admin.site.register(User)
admin.site.register(OtpVerification)
admin.site.register(Profile)