from rest_framework import serializers
from blog.models import Post

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'excerpt', 'author', 'category', 'tag')

