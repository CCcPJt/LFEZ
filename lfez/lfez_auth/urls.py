from django.conf.urls import url
from lfez_auth.views import UserControl

urlpatterns = [
	url(r'^usercontrol/(?P<slug>\w+)$', UserControl.as_view())

]
