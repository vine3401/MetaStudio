from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickName = models.CharField(max_length=50,blank=True)
    headphoto = models.ImageField(default='default/headphoto.jpg')
    class Meta(AbstractUser.Meta):
        pass