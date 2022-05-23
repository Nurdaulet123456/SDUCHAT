from django.urls import path,include
from . import views

urlpatterns = [
    path('changeProfile/', views.updateProfile, name='changeProfile'),
]