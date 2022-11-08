from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('superheros/', views.heros_index, name='heros_index'),
  path('superheros/<int:hero_id>', views.superhero_detail, name='superhero_detail'),
  path('superheros/create/', views.HeroCreate.as_view(), name='superhero_create'),
  path('supeheros/<int:pk>/update', views.HeroUpdate.as_view(), name='superhero_update'),
  path('supeheros/<int:pk>/delete', views.HeroDelete.as_view(), name='superhero_delete'),
  path('superheros/<int:hero_id>/add_movie', views.add_movie, name='add_movie'),
  path('villans/create/', views.VillanCreate.as_view(), name='villans_create'),
    path('villans/<int:pk>/', views.VillanDetail.as_view(), name='villans_detail'),
  path('villans/', views.VillanList.as_view(), name='villans_index'),
    path('villans/<int:pk>/update/', views.VillanUpdate.as_view(), name='villans_update'),
  path('villans/<int:pk>/delete/', views.VillanDelete.as_view(), name='villans_delete'),
  path('superheros/<int:hero_id>/assoc_villan/<int:villan_id>/', views.assoc_villan, name='assoc_villan'),
]