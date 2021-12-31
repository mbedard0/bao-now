from django.shortcuts import render
from .models import Dumpling 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def index(request):
  dumplings = Dumpling.objects.all()
  return render(request, 'dumplings/index.html', {'dumplings': dumplings})

def detail(request, dumpling_id):
  dumpling = Dumpling.objects.get(id=dumpling_id)
  return render(request, 'dumplings/detail.html', {'dumpling': dumpling})

class DumplingCreate(CreateView):
  model = Dumpling
  fields = '__all__'
  success_url = '/dumplings/'

class DumplingUpdate(UpdateView):
  model = Dumpling
  fields = ['filling', 'cook_type', 'country']

class DumplingDelete(DeleteView):
  model = Dumpling
  success_url = '/dumplings/'