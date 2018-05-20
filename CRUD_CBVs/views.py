from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from CRUD_CBVs.models import Movie


class MovieList(ListView):
    model = Movie


class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'genre']
    success_url = reverse_lazy('CRUD_CBVs: movie_list')


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'genre']
    success_url = reverse_lazy('CRUD_CBVs: movie_list')


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('CRUD_CBVs: movie_list')
