# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


STATUS = (
    (0,"Cerrado"),
    (1,"Activo")
)

class Actividad(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(editable=False, max_length=200, unique=True)
    contenido = models.TextField()
    tipo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=False)
    status = models.IntegerField(choices=STATUS, default=1)
    image = models.ImageField(upload_to="actividad", null=True, blank=True,
        verbose_name="Imagen")

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Actividad, self).save(*args, **kwargs)
