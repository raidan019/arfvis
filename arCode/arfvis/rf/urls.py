from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from . import views
'''
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
'''
urlpatterns = [
     path('', views.index, name = 'index'),
     path('hololens', views.hololens, name = 'hololens'),
     path('upload_pic', views.upload_pic, name = 'upload_pic'),
	 path('upload', views.upload, name = 'upload'),
     path('detail', views.detail, name = 'detail'),
     #path('detail', views.detail, name = 'detail'),
     path('addsensor', views.addsensor, name = 'addsensor'),
]

