from django.db import models
from django.urls import reverse

class Superhero(models.Model):
  name = models.CharField(max_length=100)
  universe = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("superhero_detail", kwargs={"hero_id": self.id})
  
