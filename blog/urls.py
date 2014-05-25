from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('', 
                       #main blog
                       url(r'^$', views.blogs, name='index'),
                       
                       #specific blog
                       url(r'^v/(?P<blog_id>\S+)/$', views.detail, name='detail'),
                       
                       #new blog post
                       url(r'^new/', views.new, name='new'),
                       
                       #edit blog post
                       url(r'^edit/(?P<blog_id>\S+)/$', views.edit, name='edit'),
                       
                       #delete blog post
                       url(r'^d/(?P<blog_id>\S+)/$', views.delete, name='delete'),
                       
                       )
