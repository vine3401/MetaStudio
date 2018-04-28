from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'account'

urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^user/$',views.userInfo, name="userInfo"),
    url(r'^userInfo/$', views.infoChange, name='infoChange'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)