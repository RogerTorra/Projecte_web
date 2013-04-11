from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from isobres.views import *
from gestorFestes.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='Inici'),
    # url(r'^web/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^/$', index),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^festes/$', festes),
	url(r'^festes/(?P<idFesta>\w+)', festa_info),
	url(r'^festesLocal/festa/(?P<idFesta>\w+)',festaLocal_info),
	url(r'^festesLocal/(?P<idLocal>\w+)',festes_local),
    url(r'^ciutats/$', ciutats),
	url(r'^ciutats/(?P<idCiutat>\w+)', ciutat_info),
	url(r'^locals/$',locals_view),	
	url(r'^locals/(?P<idLocal>\w+)',locals_info),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                    { 'next_page' : '/'}),
	#url(r'^login/control$', controlLogin),
    url(r'^user/(\w+)/$', userpage),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

)

if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)
