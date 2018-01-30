from django.conf.urls import url
from blog import views

app_name = "blog"

urlpatterns = [
    url(r'^blogs/', views.BlogList.as_view()),
    url(r'^blogs/(?P<pk>[0-9]+/$)', views.BlogDetail.as_view()),
]