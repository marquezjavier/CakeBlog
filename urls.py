from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cakeashes.views.home', name='home'),
    # url(r'^cakeashes/', include('cakeashes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('blog.urls', namespace='Blogs_', app_name="blog")),
    url(r'^blog/', include('blog.urls', namespace='Blogs', app_name="blog")),
    url(r'^u/', include('user.urls', namespace='Users', app_name="users")),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.STATIC_ROOT })
    
)
