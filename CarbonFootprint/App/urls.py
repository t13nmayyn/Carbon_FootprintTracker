from django.contrib import admin
from django.urls import path,include
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]