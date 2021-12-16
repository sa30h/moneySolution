from django.urls import path
from . import views

urlpatterns = [
    path('createhouseloan/',views.C_HouseloanApi.as_view()),
    path('rudhouseloan/<id>',views.RUD_HouseloanApi.as_view()),

    path('createpersonalloan/',views.C_PersonalloanApi.as_view()),
    path('rudpersonalloan/<id>',views.RUD_PersonalloanApi.as_view()),

    path('createbusinessloan/',views.C_BusinessloanApi.as_view()),
    path('rudbusinessloan/<id>',views.RUD_BusinessloanApi.as_view()),


]
