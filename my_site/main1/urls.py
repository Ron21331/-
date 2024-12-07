from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pusto),
    path('glav', views.index),
    path('vhod', views.vhod),
    path('carta', views.carta),
    path('res', views.res),
    path('Onas', views.Onas),
    path('SV', views.SV),
]