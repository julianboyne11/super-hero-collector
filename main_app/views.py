from django.shortcuts import render

from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Hero:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, universe, description,):
    self.name = name
    self.universe = universe
    self.description = description

heros = [
  Hero('Spiderman', 'Marvel', 'Spiderman, does whatever spider can'),
  Hero('Iron Man', 'Marvel', 'Tony Stark is and great innovator'),
]

def home(request):
  return HttpResponse('<h1>Hello There</h1>')

def about(request):
  return render(request, 'about.html')

def heros_index(request):
  return render(request, 'heros/index.html', {'heros': heros})

