"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from inicio import views
from django.conf import settings
from django.conf.urls.static import static
#from actividades.commands_views import StartView, AuthorCommandView, AuthorInverseListView, AuthorCommandQueryView, UnknownView, AuthorName, MessageView
#from telegrambot.handlers import command, unknown_command, regex, message

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),
    url(r'^blog/', include('blog.urls')),
    url(r'^actividades/', include('actividades.urls')),
    #url(r'^$', views.inicio, name='inicio'),
    url(r'^$', views.inicio.as_view(), name='inicio'),
    #url(r'^home/', include('home.urls'))
    #url(r'^actividades/', views.actividades, name='actividades'),
    url(r'^testimonios/', views.testimonios, name='testimonios'),
    #url(r'^blog/', views.blog, name='blog'),
    url(r'^contacto/', views.contacto, name='contacto'),
    url(r'^comments/',include('django_comments.urls')),

]

#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#https://api.telegram.org/bot1151602273:AAEDZTu8t1tcOM5pWDF6Yk4BDih_sw_L7aQ/setWebHook?url=https://soycruzmery.pythonanywhere.com/telegrambot/webhook/1151602273:AAEDZTu8t1tcOM5pWDF6Yk4BDih_sw_L7aQ/