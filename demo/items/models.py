# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models


class Item(models.Model):
    number = models.IntegerField('番号', default=0)
    name = models.CharField('名前', blank=False, null=False, max_length=255)
    description = models.CharField('説明', blank=False, null=False, max_length=255)

    def __str__(self):
        return self.name

    class Admin(admin.ModelAdmin):
        pass
