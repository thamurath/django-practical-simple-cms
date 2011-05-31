from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Example:
    # (r'^django_practical_cms/', include('django_practical_cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
         { 'document_root': '/home/feanaro/Descargas/tinymce/jscripts' }),
        
    # Para que entienda las urls de la nueva aplicacion
    (r'', include('django.contrib.flatpages.urls')),
)


#===============================================================================
# from django.conf import settings
# 
# #Esto solo lo hacemos para la version de depuracion porque si no esto es 
# #demasiado lento
# if True == settings.DEBUG:
#    urlpatterns += patterns('',
#        # Ponemos la configuracion para poder funcionar con el editor RTE
#        (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
#         { 'document_root': '/home/feanaro/workspace-cpp/django_practical_cms/src/django_practical_cms/media/tinymce/jscripts' }),
#        
#    )
#===============================================================================
