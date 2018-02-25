from django.db import models
from MetaStudio.settings import AUTH_USER_MODEL

# Create your models here.


class BlogComment(models.Model):

    text = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey("blog.Post")
    user = models.ForeignKey("account.User")

    def __str__(self):
        return self.text[:20]


class SubBComment(models.Model):
    text = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)

    parentComment = models.ForeignKey("BlogComment")
    user = models.ForeignKey("account.User",related_name="user")
    toUser = models.ForeignKey("account.User", related_name="toUser")

    def __str__(self):
        return self.text[:20]


class GameComment(models.Model):

    text = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)

    game = models.ForeignKey("game.Game")
    user = models.ForeignKey("account.User")

    def __str__(self):
        return self.text[:20]


class SubGComment(models.Model):

    text = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)

    parentComment = models.ForeignKey("GameComment")
    user = models.ForeignKey("account.User", related_name="member")
    toUser = models.ForeignKey("account.User", related_name="toMember")

    def __str__(self):
        return self.text[:20]

