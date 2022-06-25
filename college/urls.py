from django import urls
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('cportal/',views.cportal,name="cportal"),
    path('create/',views.createxam,name="create"),
    path('correction/',views.correction,name="correction")
    
]
