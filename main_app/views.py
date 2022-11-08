from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Superhero, Villan
from .forms import MovieForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def heros_index(request):
  heros = Superhero.objects.all()
  return render(request, 'heros/index.html', {'heros': heros})

@login_required
def superhero_detail(request, hero_id):
  hero = Superhero.objects.get(id=hero_id)
  villans_hero_doesnt_have = Villan.objects.exclude(id__in = hero.villans.all().values_list('id'))
  return render(request, 'heros/detail.html', { 'hero': hero, 'movie_form': MovieForm(), 'villans': villans_hero_doesnt_have})

@login_required
def add_movie(request, hero_id):
  form = MovieForm(request.POST)
  if form.is_valid():
    new_movie = form.save(commit=False)
    new_movie.superhero_id = hero_id
    new_movie.save()
  return redirect('superhero_detail', hero_id=hero_id)

@login_required
def assoc_villan(request, hero_id, villan_id):
  # Note that you can pass a toy's id instead of the whole object
  Superhero.objects.get(id=hero_id).villans.add(villan_id)
  return redirect('superhero_detail', hero_id=hero_id)

class HeroCreate(CreateView):
  model = Superhero
  fields = ['name', 'universe', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class HeroUpdate(UpdateView, LoginRequiredMixin):
  model = Superhero
  fields = ['universe', 'description']

class HeroDelete(DeleteView, LoginRequiredMixin):
  model =Superhero
  success_url = '/superheros/'

class VillanCreate(CreateView, LoginRequiredMixin):
  model = Villan
  fields = '__all__'

class VillanList(ListView, LoginRequiredMixin):
  model = Villan

class VillanDetail(DetailView, LoginRequiredMixin):
  model = Villan

class VillanUpdate(UpdateView, LoginRequiredMixin):
  model = Villan
  fields = ['name', 'description']

class VillanDelete(DeleteView, LoginRequiredMixin):
  model = Villan
  success_url = '/villans/'

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)