from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from isobres.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    # url(r'^web/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	#url(r'^media/(?P.*)$','django.views.static.serve',
	#	{'document_root':settings.MEDIA_ROOT,}
	#),
)