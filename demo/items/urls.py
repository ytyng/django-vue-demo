# -*- coding: utf-8 -*-
from django.urls import path

from . import views
from . import apis

app_name = 'items'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/items', apis.items),
    path('api/item/<int:item_id>', apis.item),
]
