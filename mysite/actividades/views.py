# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Actividad

class ActividadList(generic.ListView):
    model = Actividad
    template_name = 'listaDeActividades.html'


class ActividadDetail(generic.DetailView):
    model = Actividad
    template_name = 'detalleDeActividades.html'
