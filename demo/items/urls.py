# -*- coding: utf-8 -*-
from django.urls import path

from . import views
from . import apis

app_name = 'items'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/items', views.index, name='index'),
]
