from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickName = models.CharField(max_length=50,blank=True)
    headphoto = models.ImageField(default='default/headphoto.jpg')
    class Meta(AbstractUser.Meta):
        pass


class MessageApp(models.Model):

    mes = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)

    app = models.ForeignKey("app.App")
    user = models.ForeignKey("User", related_name="user_app")
    toUser = models.ForeignKey("User", related_name="toUser_app")

    def __str__(self):
        return self.mes


class MessageBlog(models.Model):

    mes = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)

    post = models.ForeignKey("blog.Post")
    user = models.ForeignKey("User", related_name="user_post")
    toUser = models.ForeignKey("User", related_name="toUse_post")

    def __str__(self):
        return self.mes