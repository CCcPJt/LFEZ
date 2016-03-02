from django.conf.urls import url

from . import views

urlpatterns =  [
	url(r'^$', views.index, name='index'),
	url(r'^groups$', views.groups, name='groups'),
	url(r'^activities$', views.activities, name='activities'),
	url(r'^me$', views.me, name='me'),
	url(r'^test_page$', views.test_view, name='test_view')
]
