from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Superhero, Villan
from .forms import MovieForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def heros_index(request):
  heros = Superhero.objects.all()
  return render(request, 'heros/index.html', {'heros': heros})

def superhero_detail(request, hero_id):
  hero = Superhero.objects.get(id=hero_id)
  return render(request, 'heros/detail.html', { 'hero': hero, 'movie_form': MovieForm()})

def add_movie(request, hero_id):
  form = MovieForm(request.POST)
  if form.is_valid():
    new_movie = form.save(commit=False)
    new_movie.superhero_id = hero_id
    new_movie.save()
  return redirect('superhero_detail', hero_id=hero_id)

class HeroCreate(CreateView):
  model = Superhero
  fields = '__all__'

class HeroUpdate(UpdateView):
  model = Superhero
  fields = ['universe', 'description']

class HeroDelete(DeleteView):
  model =Superhero
  success_url = '/superheros/'

class VillanCreate(CreateView):
  model = Villan
  fields = '__all__'

class VillanList(ListView):
  model = Villan

class VillanDetail(DetailView):
  model = Villan