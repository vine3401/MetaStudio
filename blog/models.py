from django.db import models
from django.contrib.auth.models import User

from account.models import User

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
    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])