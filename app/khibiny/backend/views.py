from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'index.html'
    return render(request, template) 


def about(request):
    template = 'about.html'
    return render(request, template)


def travel(request):
    template = 'travel.html'
    return render(request, template)


def polar_shine(request):
    template = 'polar_shine.html'
    return render(request, template)


def khibiny_heart(request):
    template = 'khibiny_heart.html'
    return render(request, template)


def snow_travel(request):
    template = 'snow_travel.html'
    return render(request, template)


def teriberka(request):
    template = 'teriberka.html'
    return render(request, template)


def white_sea(request):
    template = 'white_sea.html'
    return render(request, template)


def snow_walk(request):
    template = 'snow_walk.html'
    return render(request, template)


def walk(request):
    template = 'walk.html'
    return render(request, template)


def seidozero(request):
    template = 'seidozero.html'
    return render(request, template)


def art_park(request):
    template = 'art_park.html'
    return render(request, template)

def etno(request):
    template = 'etno.html'
    return render(request, template)