from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dumplings/', views.index, name='dumplings_index'),
  path('dumplings/<int:dumpling_id>/', views.detail, name='dumplings_detail'),
  path('dumplings/create/', views.DumplingCreate.as_view(), name='dumplings_create'),
  path('dumplings/<int:pk>/update/', views.DumplingUpdate.as_view(), name='dumplings_update'),
  path('dumplings/<int:pk>/delete/', views.DumplingDelete.as_view(), name='dumplings_delete'),
  path('dumplings/<int:dumpling_id>/add_fold/', views.add_fold, name='add_fold'),
  path('sauces/create/', views.SauceCreate.as_view(), name='sauces_create'),
  path('sauces/', views.SauceList.as_view(), name='sauces_index'),
  path('sauces/<int:sauce_id>//', views.SauceDetail.as_view(), name='sauces_detail')
]