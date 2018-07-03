from django.conf.urls import url
from . import views

app_name = 'submit'
urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.check, name='check')
]