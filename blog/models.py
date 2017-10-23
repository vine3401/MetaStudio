from django.db import models
from MetaStudio.settings import AUTH_USER_MODEL
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 100)
    createTime = models.DateTimeField(auto_now_add=True)
    modifiedTime = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    excerpt = models.CharField(max_length=200, blank = True)
    views = models.PositiveIntegerField(default=0) #该字段的值只允许为正整数或者0

    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)

    author = models.ForeignKey(AUTH_USER_MODEL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs = { 'pk':self.pk })

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])