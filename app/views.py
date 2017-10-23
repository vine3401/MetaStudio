from django.shortcuts import render,get_object_or_404
from .models import AppCategory, App
from comment.forms import AppCommentForm,SubACommentForm
from comment.models import SubAComment
from django.http import StreamingHttpResponse

import os, tempfile, zipfile

# Create your views here.


def portfllio(request):
    categories = AppCategory.objects.all().order_by("name")
    appList = []
    for cate in categories:
        apps = App.objects.filter(category = cate.pk).order_by("-createTime")
        temp = (cate,apps)
        appList.append(temp)

    return render(request, 'home/portfolio.html', context = {'appList':appList})


def appInfo(request,pk):
    app = get_object_or_404(App, pk=pk)
    form = AppCommentForm()
    subForm = SubACommentForm()
    c = app.appcomment_set.all()
    comments = []
    for comment in c:
        subComment = SubAComment.objects.filter(parentComment=comment.pk).order_by("createTime")
        temp = (comment,subComment)
        comments.append(temp)

    context = {
        'app': app,
        'form': form,
        'subForm': subForm,
        'comments': comments,
    }
    return render(request, 'app/app.html', context=context)



def downloadApp(request, pk):
    appObj = get_object_or_404(App, pk=pk)

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    url = str(appObj.app.url)
    name = str(appObj.app)
    response = StreamingHttpResponse(file_iterator(url))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(name)

    appObj.increase_times()
    return response


def uploadApp(request):
    pass