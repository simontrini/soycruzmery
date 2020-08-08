# -*- coding: utf-8 -*-
import telegram # this is from python-telegram-bot package

from django.conf import settings
from django.template.loader import render_to_string
#from __future__ import unicode_literals

from django.db import models

# Create your models here.
#from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


STATUS = (
    (0,"Cerrado"),
    (1,"Activo"),
    (2,"Editando")
)
class Actividad(models.Model):
    titulo = models.TextField(max_length=200, unique=True)
    slug = models.SlugField(editable=True, max_length=200, unique=True)
    contenido = models.TextField()
    tipo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=False)
    status = models.IntegerField(choices=STATUS, default=1)
    image = models.ImageField(upload_to="actividades", null=True, blank=True,
        verbose_name="Imagen")

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        if self.status == 1:
            message_html = render_to_string('telegram_message.html', {
            'post': self })
            telegram_settings = settings.TELEGRAM
            bot = telegram.Bot(token=telegram_settings['bot_token'])
            bot.send_message(chat_id="@%s" % telegram_settings['channel_name'],
            text=message_html, parse_mode=telegram.ParseMode.HTML)

        super(Actividad, self).save(*args, **kwargs)
