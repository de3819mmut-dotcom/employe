from django.shortcuts import render
from .models import Prueba

from django.views.generic import TemplateView, ListView
# Create your views here.
class IndexView(TemplateView):
  template_name = 'home/index.html'

class PruebaListView(ListView):
  template_name = 'home/lista.html'
  queryset = ['A', 'B', 'C', 'D']
  context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
  model = Prueba
  template_name = 'home/modelo_prueba.html'
  context_object_name = 'lista_modelo_prueba'