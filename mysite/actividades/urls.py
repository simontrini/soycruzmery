from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.ActividadList.as_view(), name='ActividadList'),
    url(r'^(?P<slug>[-\w]+)/$', views.ActividadDetail.as_view(), name='ActividadDetail'),
]
