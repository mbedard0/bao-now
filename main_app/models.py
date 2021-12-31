from django.db import models

# Create your models here.

class Dumpling(models.Model):
  name = models.CharField(max_length=100)
  filling = models.CharField(max_length=300)
  cook_type = models.CharField(max_length=100)
  country = models.CharField(max_length=100)