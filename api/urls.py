from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns=[
    url(r'test/$', views.Test.as_view(), name='Test'),
   
]