from datetime import datetime
from os import listdir

from django.shortcuts import render, reverse


def home_view(request):
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, 'app/home.html', context)


def time_view(request):
    current_time = datetime.now().strftime('%H:%M:%S')
    context = dict(current_time=current_time)
    return render(request, 'app/current_time.html', context)


def workdir_view(request):
    context = dict(files=listdir())
    return render(request, 'app/workdir.html', context)
