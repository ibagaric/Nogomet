from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nogomet.views.home', name='home'),
    url(r'^', include('tablica.urls')),
    url(r'^admin/', include(admin.site.urls)),
) 
