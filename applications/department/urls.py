from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "department_app"
urlpatterns = [
    path('NewDepartamentoView', views.NewDepartamentoView.as_view(),
         name='NewDepartamentoView'),
    path('ListarDepartamentos', views.ListarDepartamentos.as_view(),
         name='ListarDepartamentos'),
    path('CrearDepartamento', views.CrearDepartamento.as_view(),
         name='CrearDepartamento'),
]
