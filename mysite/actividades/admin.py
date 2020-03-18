# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import Actividad

class ActividadAdmin(SummernoteModelAdmin):
    list_display = ('titulo', 'tipo', 'fecha',,'')
    list_filter = ("status",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    summernote_fields = ('contenido',)

admin.site.register(Actividad, ActividadAdmin)


