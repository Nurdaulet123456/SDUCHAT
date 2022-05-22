from django.urls import path,include, re_path
from . import views

urlpatterns = [
    path('main/', views.index, name='main'),
    path('chat/<str:username>', views.main, name = "chat"),
    path("add_star/", views.starred_users, name="add"),
    path('starreds/', views.izbrannyie, name='starreds'),
    # path('main/<str:username>', views.mainarg, name='mainarg'),
  #  re_path(r'search_connections/(?P<data>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.filterUser, name = "filterUser"),
]