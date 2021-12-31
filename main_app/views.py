from django.shortcuts import render
from .models import Dumpling 
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