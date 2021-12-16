from django.urls import path,include

from . import views


urlpatterns = [
	path('detail/',views.EwalletDetailAPIView.as_view()),
	path('pay/',views.PayMoney.as_view())

]