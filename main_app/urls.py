from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dumplings/', views.index, name='dumplings_index'),
  path('dumplings/<int:dumpling_id>/', views.detail, name='dumplings_detail'),
  path('dumplings/create/', views.DumplingCreate.as_view(), name='dumplings_create'),
]