from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('map/', views.map, name='map'),
    path('map/result/', views.result, name='result' ),
    path('about/', views.about, name='about'),
    path('communication/', views.communication, name='communication'),
]