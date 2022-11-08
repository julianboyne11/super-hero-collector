from django.shortcuts import render
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Superhero
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

class HeroCreate(CreateView):
  model = Superhero
  fields = '__all__'

class HeroUpdate(UpdateView):
  model = Superhero
  fields = ['universe', 'description']

class HeroDelete(DeleteView):
  model =Superhero
  success_url = '/superheros/'