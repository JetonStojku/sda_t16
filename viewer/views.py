from django.http import HttpResponse
from django.shortcuts import render

from viewer.models import Movie


def hello(request):
    return HttpResponse('Hello, world!')


def hello_re(request, s):
    return HttpResponse(f'Hello, {s} world!')


def hello_encode(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')


def welcome(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def home(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='home.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def movies(request, genre=None):
    if genre:
        movie = Movie.objects.filter(genre__name=genre)
    else:
        movie = Movie.objects.all()
    return render(
        request, template_name='home.html',
        context={'movies': enumerate(movie, start=1)}
    )
