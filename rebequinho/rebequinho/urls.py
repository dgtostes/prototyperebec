from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'rebequinho.views.index'),
    #url(r'^ensaios/', 'ensaios.views.index'),
    #url(r'^revisao/', 'revisao.views.index'),
    url(r'^revisao/', include('revisao.urls')),
    url(r'^ensaios/', include('ensaios.urls')),
    # url(r'^rebequinho/', include('rebequinho.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


from django.conf import settings
if settings.DEBUG:
    # serve static files from develpment server
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )