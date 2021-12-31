from django.forms import ModelForm
from .models import Folding

class FoldingForm(ModelForm):
  class Meta:
    model = Folding
    fields = ['date', 'fold']
