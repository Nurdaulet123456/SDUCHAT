from django.urls import path,include, re_path
from . import views

urlpatterns = [
    path('roomForm/', views.roomForm, name='roomForm'),
    path('room/<slug:slug>', views.room, name='room'),
]