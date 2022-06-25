from django import urls
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('portal_st/',views.portal),
    path('test/',views.test,name="test")
]
