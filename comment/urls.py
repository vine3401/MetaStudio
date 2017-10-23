from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "comment"

urlpatterns=[
    url(r'comment/post/(?P<post_pk>[0-9]+)$', views.post_comment, name='post_comment'),
    url(r'comment/app/(?P<app_pk>[0-9]+)$', views.app_comment, name='app_comment'),
    url(r'subComment/post/(?P<post_pk>[0-9]+)/(?P<comment_pk>[0-9]+)$', views.sub_post_comment, name="sub_post_comment"),
    url(r'subComment/app/(?P<app_pk>[0-9]+)/(?P<comment_pk>[0-9]+)$', views.sub_app_comment, name="sub_app_comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)