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
     path('<int:signal_id>/', views.detail, name = 'detail'),
<<<<<<< HEAD
     path('add_sensor', views.addsensor, name = 'add_sensor'),
=======
     path('addsensor', views.addsensor, name = 'addsensor'),

>>>>>>> 3a37efedd0c0508d6100a83a2a663156d825ee25
]
