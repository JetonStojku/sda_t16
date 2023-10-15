from logging import getLogger

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView

from viewer.forms import MovieForm, MovieModelForm, GenreModelForm
from viewer.models import Movie, Genre

LOGGER = getLogger()


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
    rating = request.GET.get('rating', 0)
    if genre:
        movie = Movie.objects.filter(genre__name=genre).filter(rating__gt=rating)
    else:
        movie = Movie.objects.filter(rating__gt=rating)
    return render(
        request, template_name='home.html',
        context={'movies': enumerate(movie, start=1)}
    )


class MoviesView(View):
    def get(self, request):
        return render(
            request, template_name='all_movie.html',
            context={'movies': Movie.objects.all()}
        )


class MoviesTemplateView(TemplateView):
    template_name = 'all_movie.html'
    extra_context = {'movies': Movie.objects.all()}


class MoviesListView(ListView):
    template_name = 'list_movie.html'
    model = Movie


class GenreListView(ListView):
    template_name = 'all_genre.html'
    model = Genre


class MovieFormView(FormView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data['title'],
            genre=cleaned_data['genre'],
            rating=cleaned_data['rating'],
            released=cleaned_data['released'],
            description=cleaned_data['description']
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class MovieCreateView(CreateView):
    template_name = 'new_form.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('list')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    template_name = 'new_form.html'
    model = Movie
    form_class = MovieModelForm
    success_url = reverse_lazy('list')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)


class MovieDeleteView(DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('list')


class GenreCreateView(CreateView):
    template_name = 'genre_form.html'
    form_class = GenreModelForm
    success_url = reverse_lazy('genre')


class GenreUpdateView(UpdateView):
    template_name = 'genre_form.html'
    model = Genre
    form_class = GenreModelForm
    success_url = reverse_lazy('genre')


class GenreDeleteView(DeleteView):
    template_name = 'genre_confirm_delete.html'
    model = Genre
    success_url = reverse_lazy('genre')
