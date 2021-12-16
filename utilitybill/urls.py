from django.urls import path
from . import views
urlpatterns = [
    path('createphonebill/',views.C_PhonebillApi.as_view()),
    path('rudphonebill/<id>',views.RUD_PhonebillApi.as_view()),
    path('createinternetbill/',views.C_InternetbillApi.as_view()),
    path('rudinternetbill/<id>',views.RUD_InternetbillApi.as_view()),
    path('createwaterbill/',views.C_WaterbillApi.as_view()),
    path('rudwaterbill/<id>',views.RUD_WaterbillApi.as_view()),
    path('createelectricity/',views.C_ElectricitybillApi.as_view()),
    path('rudphonebill/<id>',views.RUD_ElectricitybillApi.as_view()),
]
