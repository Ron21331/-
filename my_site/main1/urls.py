from django.urls import path, include
from . import views

urlpatterns = [
    path('apl/', views.glav, name='glav'),
    path('apl/carta/', views.carta, name='carta'),
    path('apl/carta/res/', views.res, name='res' ),
    path('apl/onas/', views.Onas, name='onas'),
    path('apl/sv/', views.SV, name='sv'),
]