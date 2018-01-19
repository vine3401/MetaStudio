from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "comment"

urlpatterns=[
    url(r'comment/post/(?P<post_pk>[0-9]+)$', views.post_comment, name='post_comment'),
    url(r'comment/game/(?P<app_pk>[0-9]+)$', views.game_comment, name='game_comment'),
    url(r'subComment/post/(?P<post_pk>[0-9]+)/(?P<comment_pk>[0-9]+)$', views.sub_post_comment, name="sub_post_comment"),
    url(r'subComment/game/(?P<game_pk>[0-9]+)/(?P<comment_pk>[0-9]+)$', views.sub_game_comment, name="sub_game_comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)