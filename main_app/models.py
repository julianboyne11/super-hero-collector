from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Villan(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse('villans_detail', kwargs={"pk": self.id})
  

class Superhero(models.Model):
  name = models.CharField(max_length=100)
  universe = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  villans = models.ManyToManyField(Villan)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("superhero_detail", kwargs={"hero_id": self.id})
  
class Movie(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField('Release date')

  superhero = models.ForeignKey(Superhero, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.title} released {self.date}"

  class Meta:
    ordering = ['-date']


