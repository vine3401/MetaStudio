from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .forms import BlogCommentForm, AppCommentForm, SubBCommentForm, SubACommentForm
from app.models import App
from account.models import User
from .models import BlogComment, AppComment, SubBComment,SubAComment
from account.models import MessageApp,MessageBlog
# Create your views here.


def post_comment(request,post_pk):

    post = get_object_or_404(Post, pk=post_pk)
    user = get_object_or_404(User,pk=request.user.pk)

    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()
            # MessageBlog.objects.create(mes=request.POST['text']', user=user,toUser='',post=post)
            return redirect(post)
        else:
            c = post.blogcomment_set.all()
            subForm = SubBCommentForm()
            form = BlogCommentForm()
            comments = []
            for comment in c:
                subComment = SubBComment.objects.filter(parentComment=comment.pk).order_by("createTime")
                temp = (comment, subComment)
                comments.append(temp)
            context = {'post': post,
                       'form': form,
                       'subForm': subForm,
                       'comments': comments,
                       }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)


def sub_post_comment(request, post_pk, comment_pk):

    post = get_object_or_404(Post, pk=post_pk)
    parent = get_object_or_404(BlogComment, pk=comment_pk)

    if request.method == 'POST':
        form = SubBCommentForm(request.POST)
        if form.is_valid():
            subComment = form.save(commit=False)
            subComment.parentComment = parent
            subComment.save()
            return redirect(post)
        else:
            form = BlogCommentForm()
            subForm = SubBCommentForm()
            c = post.blogcomment_set.all()
            comments = []
            for comment in c:
                subComment = SubBComment.objects.filter(parentComment=comment.pk).order_by("createTime")
                temp = (comment, subComment)
                comments.append(temp)

            context = {'post': post,
                       'form': form,
                       'subForm':subForm,
                       'comments': comments,
                       }
            return render(request, 'blog/detail.html', context=context)

    return redirect(post)


def app_comment(request, app_pk):

    app = get_object_or_404(App, pk=app_pk)
    user = get_object_or_404(User, pk=request.user.pk)

    if request.method == 'POST':
        form = AppCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.app = app
            comment.user = user
            comment.save()
            return redirect(app)
        else:
            c = app.appcomment_set.all()
            form = AppCommentForm()
            subForm = SubACommentForm()
            comments = []
            for comment in c:
                subComment = SubAComment.objects.filter(parentComment=comment.pk).order_by("createTime")
                temp = (comment, subComment)
                comments.append(temp)

            context = {'app': app,
                       'form': form,
                       'subForm': subForm,
                       'comments': comments,
                       }
            return render(request, 'app/app.html', context=context)
    return redirect(app)


def sub_app_comment(request, app_pk, comment_pk):

    app = get_object_or_404(App, pk=app_pk)
    parent = get_object_or_404(AppComment, pk=comment_pk)

    if request.method == 'POST':
        form = SubACommentForm(request.POST)
        if form.is_valid():
            subComment = form.save(commit=False)
            subComment.parentComment = parent
            subComment.save()
            print("this")
            return redirect(app)
        else:
            print("this")
            form = AppCommentForm()
            subForm = SubACommentForm()
            c = app.appcomment_set.all()
            comments = []
            for comment in c:
                subComment = SubAComment.objects.filter(parentComment=comment.pk).order_by("createTime")
                temp = (comment, subComment)
                comments.append(temp)

            context = {'app': app,
                       'form': form,
                       'subForm': subForm,
                       'comments': comments,
                       }
            return render(request, 'app/app.html', context=context)

    return redirect(app)