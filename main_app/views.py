from typing import List
from django.shortcuts import render, redirect
from .models import Dumpling, Folding, Sauce
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FoldingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required(login_url='/')
def index(request):
  dumplings = Dumpling.objects.filter(user=request.user)
  return render(request, 'dumplings/index.html', {'dumplings': dumplings})

@login_required(login_url='/')
def detail(request, dumpling_id):
  dumpling = Dumpling.objects.get(id=dumpling_id)
  sauces_dumpling_doesnt_have = Sauce.objects.exclude(id__in = dumpling.sauces.all().values_list('id'))
  folding_form = FoldingForm()
  return render(request, 'dumplings/detail.html', {'dumpling': dumpling, 'folding_form': FoldingForm(), 'sauces': sauces_dumpling_doesnt_have})

@login_required(login_url='/')
def add_fold(request, dumpling_id):
  form = FoldingForm(request.POST)
  if form.is_valid():
    new_folding = form.save(commit=False)
    new_folding.dumpling_id = dumpling_id
    new_folding.save()
  return redirect('dumplings_detail', dumpling_id=dumpling_id)

@login_required(login_url='/')
def assoc_sauce(request, dumpling_id, sauce_id):
  Dumpling.objects.get(id=dumpling_id).sauces.add(sauce_id)
  return redirect('dumplings_detail', dumpling_id=dumpling_id)

class DumplingCreate(CreateView):
  login_url = '/'
  model = Dumpling
  fields = '__all__'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  success_url = '/dumplings/'

def signup(request):
  login_url = '/'
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('dumplings_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class DumplingUpdate(UpdateView):
  login_url = '/'
  model = Dumpling
  fields = ['filling', 'cook_type', 'country']

class DumplingDelete(DeleteView):
  login_url = '/'
  model = Dumpling
  success_url = '/dumplings/'

class SauceCreate(CreateView):
  login_url = '/'
  model = Sauce
  fields = '__all__'

class SauceList(ListView):
  login_url = '/'
  model = Sauce

class SauceDetail(DetailView):
  login_url = '/'
  model = Sauce

class SauceUpdate(UpdateView):
  login_url = '/'
  model = Sauce
  fields = ['ingredients']

class SauceDelete(DeleteView):
  login_url = '/'
  model = Sauce
  success_url = '/sauces/'

