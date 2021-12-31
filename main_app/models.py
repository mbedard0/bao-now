from django.db import models
from django.urls import reverse

# Create your models here.

class Dumpling(models.Model):
  name = models.CharField(max_length=100)
  filling = models.CharField(max_length=300)
  cook_type = models.CharField(max_length=100)
  country = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('dumplings_detail', kwargs={'dumpling_id': self.id})