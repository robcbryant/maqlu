from django.conf.urls import url
from . import views

app_name = 'enki'
urlpatterns = [
	# ex: /enki/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# ex: /enki/5/
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]