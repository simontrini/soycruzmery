# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from actividades.models import Actividad

class inicio(generic.ListView):
    model = Actividad
    template_name = 'inicio.html'

#def inicio(request):
#    return render(request, 'inicio.html', {'poll': 'hola'})

#def actividades(request):
#    return render(request, 'actividades.html', {'poll': 'hola'})

def testimonios(request):
    return render(request, 'testimonios.html', {'poll': 'hola'})

#def blog(request):
#    return render(request, 'blog.html', {'poll': 'hola'})

def contacto(request):
    return render(request, 'contacto.html', {'poll': 'hola'})