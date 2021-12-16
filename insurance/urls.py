from django.urls import path
from . import views

urlpatterns = [
    path('createcarinsurancepay/',views.C_CarinsuraceApi.as_view()),
    path('rudcarinsurancepay/<id>',views.RUD_CarinsuranceApi.as_view()),

    path('createhouseinsurancepay/',views.C_HouseinsuranceApi.as_view()),
    path('rudhouseinsurancepay/<id>',views.RUD_HouseinsuranceApi.as_view()),

    path('createpersonalinsurancepay/',views.C_PersonalinsuranceApi.as_view()),
    path('rudpersonalinsurancepay/<id>',views.RUD_PersonalinsuranceApi.as_view()),

    path('createtravelinsurancepay/',views.C_TravelinsuranceApi.as_view()),
    path('rudtravelinsurancepay/<id>',views.RUD_TravelinsuranceApi.as_view()),

]
