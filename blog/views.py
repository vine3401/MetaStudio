from django.shortcuts import render,get_object_or_404, redirect
from .models import Category, Tag, Post
from app.models import AppCategory, App
from comment.forms import BlogCommentForm,SubBCommentForm
from comment.models import BlogComment,SubBComment
from .forms import PostForm


def index(request):
    posts = Post.objects.all().order_by("-createTime")[:5]
    apps = App.objects.all().order_by("-createTime")[:3]
    context = {
        'posts': posts,
        'apps': apps,
    }
    return render(request, 'home/index.html', context = context)

def blog(request):
    categories = Category.objects.all().order_by("name")
    postList = []
    for cate in categories:
        posts = Post.objects.filter(category=cate.pk).order_by("-createTime")
        temp = (cate,posts)
        postList.append(temp)
    context = {
        "categories": categories,
        "postList": postList,
    }
    return render(request, 'home/blog.html', context = context)

def about(request):
    return render(request, 'home/about.html', context = None)

def contact(request):
    return render(request, 'home/contact.html', context = None)

def detail(request,pk):

    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    form = BlogCommentForm()
    subForm = SubBCommentForm()
    c = post.blogcomment_set.all()
    comments = []

    for comment in c:
        subComment = SubBComment.objects.filter(parentComment=comment.pk).order_by("createTime")
        temp = (comment,subComment)
        comments.append(temp)

    context = {
        'post': post,
        'form': form,
        'subForm': subForm,
        'comments': comments,
    }

    return render(request, 'blog/detail.html', context=context)


def write(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("/")
    else:
        form = PostForm()

    return render(request, 'blog/write.html', context={'form': form, 'categories': categories, 'tags': tags})