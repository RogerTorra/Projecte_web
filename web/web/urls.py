from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from isobres.views import *
from gestorFestes.views import *
#FORMS
from gestorFestes.forms import CiutatForm
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='Inici'),
    # url(r'^web/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^/$', index),
	url(r'^admin/', include(admin.site.urls)),
    #Create Festa
    url(r'^festes/create$', FestaCreate.as_view(),name='festa_create'),
	#Modificar Festa
	url(r'^festa/(?P<pk>\d+)/edit$', LocalUpdate.as_view(),name='festa_edit'),
    url(r'^festes/$', festes),
	url(r'^festes/(?P<idFesta>\w+)', festa_info, name='festa_detail'),
	url(r'^festesLocal/festa/(?P<idFesta>\w+)',festa_info),
	url(r'^festesLocal/(?P<idLocal>\w+)',festes_local),
     #Create city
    url(r'^ciutats/create$', CiutatCreate.as_view(),name='ciutat_create'),
	#Modificar ciutat
	url(r'^ciutats/(?P<pk>\d+)/edit$', CiutatUpdate.as_view(),name='ciutat_edit'),
    url(r'^ciutats/$', ciutats),
	url(r'^ciutats/(?P<idCiutat>\w+)$', ciutat_info,name='ciutat_detail'),
    
	

	#Create Local
    url(r'^locals/create$', LocalCreate.as_view(),name='local_create'),
	#Modificar Local
	url(r'^locals/(?P<pk>\d+)/edit$', LocalUpdate.as_view(),name='local_edit'),
	url(r'^locals/(?P<pk>\d+)/delete$', LocalDelete.as_view(),name='local_delete'),
    url(r'^locals/(?P<idLocal>\w+)/$',locals_info, name='local_detail'),
	
	
	url(r'^locals/$',locals_view, name='local_list'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                    { 'next_page' : '/'}),
	#url(r'^login/control$', controlLogin),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

)

#RESTful API
urlpatterns += patterns('',
	url(r'^api/locals/$', APILocalList.as_view(), name='local-list'),
	url(r'^api/locals/(?P<pk>\d+)/$', APILocalDetail.as_view(), name='local-detail'),
	url(r'^api/ciutats/$', APICiutatList.as_view(), name='ciutat-list'),
	url(r'^api/ciutats/(?P<pk>\d+)/$', APICiutatDetail.as_view(), name='ciutat-detail'),
	url(r'^api/festes/$', APIFestaList.as_view(), name='festa-list'),
	url(r'^api/festes/(?P<pk>\d+)/$', APIFestaDetail.as_view(), name='festa-detail'),
)

if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)
