from django.shortcuts import render
from .models import Prueba
from django.urls import reverse_lazy
from .forms import PruebaForm
from django.views.generic import TemplateView, ListView, CreateView
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


class PruebaCreateViewHome(CreateView):
    model = Prueba
    template_name = "home/PruebaHomeCreate.html"
    # fields = ['nombre','apellido','edad','fecha_nacimiento']
    form_class = PruebaForm
    success_url = reverse_lazy('home_app:SuccesView')


class SuccesView(TemplateView):
    template_name = "home/successView.html"


class Home(TemplateView):
    template_name = "home/index.html"
