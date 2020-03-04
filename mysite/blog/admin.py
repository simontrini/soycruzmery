# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
#from django_summernote.admin import SummernoteModelAdmin
from .models import Post

#class PostAdmin(SummernoteModelAdmin):
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'status','creado_on')
    list_filter = ("status",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    #summernote_fields = ('contenido',)

    #summernote_fields = '__all__'

admin.site.register(Post, PostAdmin)
