from django.shortcuts import render,get_object_or_404, redirect
from .models import Category, Tag, Post
from game.models import GameCategory, Game
from comment.forms import BlogCommentForm,SubBCommentForm
from comment.models import BlogComment,SubBComment
from .forms import PostForm

def index(request):
    posts = Post.objects.all().order_by("-createTime")[:5]
    games = Game.objects.all().order_by("-createTime")[:3]
    context = {
        'posts': posts,
        'games': games,
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
        print(request.POST)
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()

    return render(request, 'blog/write.html', context={'form': form, 'categories': categories, 'tags': tags})


def delete(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect("/user/")


def edit(request, pk):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    post=get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        content = request.POST
        print(content)
        post.title = content['title']
        post.category.pk = content['category']
        post.tag.pk = content['tag']
        post.body = content['body']
        post.save()
        return redirect("/user")

    context = {'post': post, 'categories': categories, 'tags': tags}

    return render(request, 'blog/edit.html', context=context)