from typing import List
from django.shortcuts import render, redirect
from .models import Dumpling, Folding, Sauce
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FoldingForm

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
  folding_form = FoldingForm()
  return render(request, 'dumplings/detail.html', {'dumpling': dumpling, 'folding_form': FoldingForm()})

def add_fold(request, dumpling_id):
  form = FoldingForm(request.POST)
  if form.is_valid():
    new_folding = form.save(commit=False)
    new_folding.dumpling_id = dumpling_id
    new_folding.save()
  return redirect('dumplings_detail', dumpling_id=dumpling_id)

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

class SauceCreate(CreateView):
  model = Sauce
  fields = '__all__'

class SauceList(ListView):
  model = Sauce

class SauceDetail(DetailView):
  model = Sauce
