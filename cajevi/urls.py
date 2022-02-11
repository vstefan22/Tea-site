from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'cajevi'
urlpatterns = [
   path('', views.index, name='index'),
   path('meni/', views.meni, name='meni'),
   path('meni/<int:pk>/', views.caj, name='caj'),
   path('search/', views.search, name='search'),
   path('narudzba/', views.narudzba, name='narudzba'),
   path('onama/', views.o_nama, name='onama'),

]