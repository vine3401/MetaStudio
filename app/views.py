from django.shortcuts import render,get_object_or_404, redirect
from .models import AppCategory, App
from comment.forms import AppCommentForm,SubACommentForm
from comment.models import SubAComment
from django.http import StreamingHttpResponse
from .forms import UploadAppForm
from django.core.files.base import ContentFile

# Create your views here.


def portfllio(request):
    categories = AppCategory.objects.all().order_by("name")
    appList = []
    for cate in categories:
        apps = App.objects.filter(category = cate.pk).order_by("-createTime")
        temp = (cate,apps)
        appList.append(temp)

    return render(request, 'home/portfolio.html', context={'appList': appList})


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
    categories = AppCategory.objects.all()

    if request.method == 'POST':
        form = UploadAppForm(request.POST)
        application = request.FILES['app']

        if form.is_valid():
            app = form.save(commit=False)
            app.app = application
            if 'icon' not in request.POST:
                app.icon = request.FILES['icon']
            if 'foreImg' not in request.POST:
                app.foreImg = request.FILES['foreImg']
            app.save()
            return redirect('/')
    else:
        form = UploadAppForm()
    return render(request, 'app/upload.html', context={'form': form, 'categories': categories})


def deleteApp(request, pk):
    App.objects.filter(pk=pk).delete()
    return redirect("/user/")

def editApp(request, pk):
    categories = AppCategory.objects.all()
    app = get_object_or_404(App, pk=pk)

    if request.method == 'POST':
        content = request.POST
        app.name = content['name']
        app.version = content['version']
        app.category.pk = content['category']
        app.inTro = content['inTro']
        if 'icon' not in request.POST:
            app.icon = request.FILES['icon']
        if 'foreImg' not in request.POST:
            app.foreImg = request.FILES['foreImg']
        if 'app' not in request.POST:
            app.app = request.FILES['app']
        app.save()
        return redirect("/user/")
    context = {'categories': categories,'app': app}

    return render(request, 'app/edit.html',context=context)