from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from tamagotchi.cat import Cat
from tamagotchi.db import Database


def cat_stats_view(request: WSGIRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        Database.add(name)
    elif request.method == 'GET':
        cat = Cat.cat_actions(cat=Database.cats[-1], action=request.GET.get('action'))
        Database.cats[-1] = cat
    return render(request, 'cat_stats.html', context={'cat': Database.cats[-1], 'actions': Database.actions})
