from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AlisenBlog.views.home', name='home'),
    # url(r'^AlisenBlog/', include('AlisenBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #-------------------------------------------------------------------------
    #Base PAges
    #-------------------------------------------------------------------------
    #Home
    url(r'^$', 'blog.views.page_home', 
        name='home'),
)

#Setup URLs
if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

