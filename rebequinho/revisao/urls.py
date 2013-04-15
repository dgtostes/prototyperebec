from django.conf.urls import patterns, url

from revisao import views

urlpatterns = patterns('',
    # ex: /revisao/
    url(r'^$', 'revisao.views.index'),
    #url(r'^$', views.index, name='index'),
)