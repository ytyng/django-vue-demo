# -*- coding: utf-8 -*-
import os

from django.contrib import admin
from django.urls import include, path
from django.views import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    # 本番は nginx とか S3 で
    path('', static.serve, kwargs={
        'path': 'index.html',
        'document_root': os.path.join(settings.BASE_DIR, 'demo/statics')}),
]
