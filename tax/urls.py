from django.urls import path
from . import views

urlpatterns = [
    path('createtax/',views.C_TaxpaymentView.as_view()),
    path('rudtax/<pk>',views.RUD_TaxpaymentView.as_view())

]
