from django.urls import path
from . import views
urlpatterns = [
    path('createmerchant/',views.CreateMerchantApiView.as_view()),
    path('rudMerchant/<merchant_name>',views.RUD_MerchatApiView.as_view()),
]