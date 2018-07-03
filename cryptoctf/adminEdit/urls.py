from django.conf.urls import url
from . import views

app_name = 'adminEdit'
urlpatterns = [
    url(r'login$', views.do_login, name='login'),
    url(r'list$', views.challengeList, name='list'),
    url(r'edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'add$', views.add, name='add'),
    url(r'download/(?P<id>\d+)/$', views.download, name='download')
]  