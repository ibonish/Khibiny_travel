from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import TravelCard


def index(request):
    template = 'index.html'
    tours = TravelCard.objects.all()[:6]
    return render(request, template, {'tours': tours})


def about(request):
    template = 'about.html'
    return render(request, template)


def summer_travel(request):
    template = 'summer_travel.html'
    summer_tours = TravelCard.objects.filter(season="summer")
    return render(request, template, {'tours': summer_tours})


def winter_travel(request):
    template = 'winter_travel.html'
    winter_tours = TravelCard.objects.filter(season="winter")
    return render(request, template, {'tours': winter_tours})


def travel_detail(request, travel_id):
    tour = get_object_or_404(TravelCard, id=travel_id)
    template = 'travel_detail.html'
    context = {
        'tour': tour,
    }
    return render(request, template, context)
