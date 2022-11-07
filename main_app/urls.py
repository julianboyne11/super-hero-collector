from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('superheros/', views.heros_index, name='heros_index'),
  path('superheros/<int:hero_id>', views.superhero_detail, name='superhero_detail'),
  path('superheros/create/', views.HeroCreate.as_view(), name='superhero_create'),
]