from django.conf.urls import patterns, url

from ensaios import views

urlpatterns = patterns('',
    # ex: /ensaios/
    url(r'^$', views.index, name='index'),
)