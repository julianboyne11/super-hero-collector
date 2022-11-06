from django.shortcuts import render
from .models import Superhero


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def heros_index(request):
  heros = Superhero.objects.all()
  return render(request, 'heros/index.html', {'heros': heros})

def superhero_detail(request, hero_id):
  hero = Superhero.objects.get(id=hero_id)
  return render(request, 'heros/detail.html', { 'hero': hero })
