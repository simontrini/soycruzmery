# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    subido_on = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    creado_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to="blog", null=True, blank=True,
        verbose_name="Imagen")

    class Meta:
        ordering = ['-creado_on']

    def __str__(self):
        return self.titulo