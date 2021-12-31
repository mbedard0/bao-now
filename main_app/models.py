from django.db import models
from django.urls import reverse

# Create your models here.

FOLDS = (
  ('M', 'Morning'),
  ('N', 'Noon'),
  ('E', 'Evening')
)

class Dumpling(models.Model):
  name = models.CharField(max_length=100)
  filling = models.CharField(max_length=300)
  cook_type = models.CharField(max_length=100)
  country = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('dumplings_detail', kwargs={'dumpling_id': self.id})

class Folding(models.Model):
  date = models.DateField('Folding date')
  fold = models.CharField(
    max_length=1,
    choices=FOLDS,
    default=FOLDS[0][0]
    )

  dumpling = models.ForeignKey(Dumpling, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_fold_display()} on {self.date}"

  class Meta:
    ordering = ['-date']