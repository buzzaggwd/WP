from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myname/', views.myname_index, name='myname'),
    path('mygroup/', views.mygroup_index, name='mygroup'),
    path('myage/', views.myage_index, name='myage'),
    path('common/', views.common, name='common'),
]