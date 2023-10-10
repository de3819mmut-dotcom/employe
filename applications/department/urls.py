from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "department_app"
urlpatterns = [
    path('NewDepartamentoView', views.NewDepartamentoView.as_view(),
         name='NewDepartamentoView'),
]
