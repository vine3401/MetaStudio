from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .forms import RegisterForm
from blog.models import Post, Category
from app.models import App
# Create your views here.


def userInfo(request):
    posts = Post.objects.filter(author=request.user.pk).order_by("-createTime")
    apps = App.objects.filter(author=request.user.pk).order_by("-createTime")
    context = {
        'posts': posts,
        'apps': apps
    }
    return render(request, 'account/user.html',context=context)


def register(request):
    redirect_to = request.POST.get("next", request.GET.get('next', ''))
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect("/")
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', context={'form': form, 'next': redirect_to})