from django.urls import path, include
from . import views

urlpatterns = [
    path('glav', views.index),
    path('carta', views.carta),
    path('res', views.res),
    path('Onas', views.Onas),
    path('SV', views.SV),
]