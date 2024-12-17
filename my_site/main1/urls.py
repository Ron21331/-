from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.glav, name='glav'),
    path('carta/', views.carta, name='carta'),
    path('res/', views.res, name='res' ),
    path('onas/', views.Onas, name='onas'),
    path('sv/', views.SV, name='sv'),
]