
#from django import views
from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.index, name='register'),
    path('', views.sigIn, name='sigin'),
    path('logout/', views.log_out, name='logout'),
]