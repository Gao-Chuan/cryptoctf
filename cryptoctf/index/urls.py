from django.conf.urls import url
from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^contributors', views.contributors, name='contributors')
]
