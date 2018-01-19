from django.shortcuts import render,get_object_or_404, redirect
from .models import GameCategory, Game
from comment.forms import GameCommentForm,SubGCommentForm
from comment.models import SubGComment
from django.http import StreamingHttpResponse
from .forms import UploadGameForm
from django.core.files.base import ContentFile

# Create your views here.


def portfllio(request):
    categories = GameCategory.objects.all().order_by("name")
    gameList = []
    for cate in categories:
        games = Game.objects.filter(category = cate.pk).order_by("-createTime")
        temp = (cate,games)
        gameList.gameend(temp)

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
        comments.gameend(temp)

    context = {
        'game': game,
        'form': form,
        'subForm': subForm,
        'comments': comments,
    }
    return render(request, 'game/game.html', context=context)

def downloadGame(request, pk):
    gameObj = get_object_or_404(Game, pk=pk)

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    url = str(gameObj.game.url)
    name = str(gameObj.game)
    response = StreamingHttpResponse(file_iterator(url))
    response['Content-Type'] = 'gamelication/octet-stream'
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