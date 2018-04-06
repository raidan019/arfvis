from django.contrib import admin
from django.conf.urls import url, paths

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
]
