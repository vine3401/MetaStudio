from django.shortcuts import render
from rest_framework import generics

from blog.models import Post
from blog.serializers import BlogSerializer

# Create your views here.
class BlogList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
