from django.urls import path
from . import views

urlpatterns = [
    path('createbillingprofile/',views.BillingProfileAPIView.as_view())
]
