# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {}
    return render(request, 'items/index.html', context)
