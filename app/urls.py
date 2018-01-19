from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'app'

urlpatterns=[
    url(r'^portfolio.html$', views.portfllio, name='portfolio'),
    url(r'^app/(?P<pk>[0-9]+)', views.appInfo, name='appInfo'),
    url(r'^download/app/(?P<pk>[0-9]+)', views.downloadApp, name='downloadApp'),
    url(r'^upload/app/$', views.uploadApp, name='uploadApp'),
    url(r'^delete/App/(?P<pk>[0-9]+)', views.deleteApp, name='deleteApp'),
    url(r'^edit/App/(?P<pk>[0-9]+)', views.editApp, name='editApp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)