from django import urls
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
    path('cportal/',views.cportal,name="cportal"),
    path('create/',views.createxam,name="create"),
    path('correction/',views.correction,name="correction"),
    path('result/',views.result,name="result")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)