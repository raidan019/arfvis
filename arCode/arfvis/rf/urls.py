from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

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
]
