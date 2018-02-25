from django.conf.urls import url
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from . import views
from MetaStudio.settings import MEDIA_ROOT

app_name = "blog"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^blog.html$', views.blog, name='blog'),
    url(r'^contact.html$', views.contact, name='contact'),
    url(r'^post/(?P<pk>[0-9]+)', views.detail, name='detail'),
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url(r'^write/', views.write, name='write'),
    url(r'^post/delete/(?P<pk>[0-9]+)', views.delete, name='delete'),
    url(r'^post/edit/(?P<pk>[0-9]+)', views.edit, name='edit'),
    # url(r'^upload', views.uploadImage, name="UploadImage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)