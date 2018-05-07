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
     path('<int:signal_id>/', views.detail, name = 'detail'),
<<<<<<< HEAD
     path('addsensor', views.addsensor, name = 'addsensor'),
=======
     path('addsensor', views.addsensor, name = 'addsensor')
>>>>>>> 0168b3030e7111742c985a3d8f3572e0206ac0b9
]
