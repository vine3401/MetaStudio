from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .forms import BlogCommentForm, GameCommentForm, SubBCommentForm, SubGCommentForm
from game.models import Game
from account.models import User
from .models import BlogComment, GameComment, SubBComment,SubGComment
from account.models import MessageGame,MessageBlog
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


def game_comment(request, game_pk):

    game = get_object_or_404(Game, pk=game_pk)
    user = get_object_or_404(User, pk=request.user.pk)

    if request.method == 'POST':
        form = GameCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.game = game
            comment.user = user
            comment.save()
            return redirect(game)
        else:
            c = game.gamecomment_set.all()
            form = GameCommentForm()
            subForm = SubGCommentForm()
            comments = []
            for comment in c:
                subComment = SubGComment.objects.filter(parentComment=comment.pk).order_by("createTime")
                temp = (comment, subComment)
                comments.append(temp)

            context = {'game': game,
                       'form': form,
                       'subForm': subForm,
                       'comments': comments,
                       }
            return render(request, 'game/game.html', context=context)
    return redirect(game)


def sub_game_comment(request, game_pk, comment_pk):

    game = get_object_or_404(Game, pk=game_pk)
    parent = get_object_or_404(GameComment, pk=comment_pk)

    if request.method == 'POST':
        form = SubGCommentForm(request.POST)
        if form.is_valid():
            subComment = form.save(commit=False)
            subComment.parentComment = parent
            subComment.save()
            return redirect(game)
        else:
            form = GameCommentForm()
            subForm = SubGCommentForm()
            c = game.gamecomment_set.all()
            comments = []
            for comment in c:
                subComment = SubGComment.objects.filter(parentComment=comment.pk).order_by("createTime")
                temp = (comment, subComment)
                comments.append(temp)

            context = {'game': game,
                       'form': form,
                       'subForm': subForm,
                       'comments': comments,
                       }
            return render(request, 'game/game.html', context=context)

    return redirect(game)