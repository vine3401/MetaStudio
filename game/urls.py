from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'game'

urlpatterns=[
    url(r'^portfolio.html$', views.portfllio, name='portfolio'),
    url(r'^game/(?P<pk>[0-9]+)', views.gameInfo, name='gameInfo'),
    url(r'^download/Game/(?P<pk>[0-9]+)', views.downloadGame, name='downloadGame'),
    url(r'^upload/Game/$', views.uploadGame, name='uploadGame'),
    url(r'^delete/Game/(?P<pk>[0-9]+)', views.deleteGame, name='deleteGame'),
    url(r'^edit/Game/(?P<pk>[0-9]+)', views.editGame, name='editGame'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)