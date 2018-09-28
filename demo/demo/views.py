# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
    return redirect(reverse('items:index'))
