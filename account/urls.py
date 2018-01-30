from django.conf.urls import url
from account import views
app_name = 'account'

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+/$)', views.UserDetail.as_view())
]