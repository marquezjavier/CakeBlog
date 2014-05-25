from django.conf.urls import patterns, url

from user import views

urlpatterns = patterns('', 
                       
                       #logout
                       url(r'^logout/', views.logoutView, name='logout'),
                       
                       #login
                       url(r'^login/', views.loginView, name='login'),
                       
                       #signup
                       url(r'^signup/', views.createUserView, name='signup'),
                       )
