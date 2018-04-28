import os

from django.shortcuts import render,get_object_or_404, redirect
from django.http import FileResponse

from .models import GameCategory, Game
from comment.forms import GameCommentForm,SubGCommentForm
from comment.models import SubGComment
from .forms import UploadGameForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def portfllio(request):
    categories = GameCategory.objects.all().order_by("name")
    gameList = []
    for cate in categories:
        games = Game.objects.filter(category = cate.pk).order_by("-createTime")
        temp = (cate,games)
        gameList.append(temp)

    return render(request, 'home/portfolio.html', context={'gameList': gameList})


def gameInfo(request,pk):
    game = get_object_or_404(Game, pk=pk)
    form = GameCommentForm()
    subForm = SubGCommentForm()
    c = game.gamecomment_set.all()
    comments = []
    for comment in c:
        subComment = SubGComment.objects.filter(parentComment=comment.pk).order_by("createTime")
        temp = (comment,subComment)
        comments.append(temp)

    context = {
        'game': game,
        'form': form,
        'subForm': subForm,
        'comments': comments,
    }
    return render(request, 'game/game.html', context=context)

def downloadGame(request, pk):
    gameObj = get_object_or_404(Game, pk=pk)
    url = BASE_DIR+str(gameObj.game.url).replace('/', '\\')
    name = str(gameObj.game)
    file = open(url, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(name)

    gameObj.increase_times()
    return response

def uploadGame(request):
    categories = GameCategory.objects.all()

    if request.method == 'POST':
        form = UploadGameForm(request.POST)
        gamelication = request.FILES['game']

        if form.is_valid():
            game = form.save(commit=False)
            game.game = gamelication
            if 'icon' not in request.POST:
                game.icon = request.FILES['icon']
            if 'foreImg' not in request.POST:
                game.foreImg = request.FILES['foreImg']
            game.save()
            return redirect('/')
    else:
        form = UploadGameForm()
    return render(request, 'game/upload.html', context={'form': form, 'categories': categories})

def deleteGame(request, pk):
    Game.objects.filter(pk=pk).delete()
    return redirect("/user/")

def editGame(request, pk):
    categories = GameCategory.objects.all()
    game = get_object_or_404(Game, pk=pk)

    if request.method == 'POST':
        content = request.POST
        game.name = content['name']
        game.version = content['version']
        game.category.pk = content['category']
        game.inTro = content['inTro']
        if 'icon' not in request.POST:
            game.icon = request.FILES['icon']
        if 'foreImg' not in request.POST:
            game.foreImg = request.FILES['foreImg']
        if 'game' not in request.POST:
            game.game = request.FILES['game']
        game.save()
        return redirect("/user/")
    context = {'categories': categories,'game': game}

    return render(request, 'game/edit.html',context=context)