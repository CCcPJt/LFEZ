from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'lfez.views.home', name='home'),
    url(r'', include('forum.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('lfez.auth'),
]
