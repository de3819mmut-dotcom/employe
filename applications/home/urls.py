from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "home_app"

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path('PruebaCreateViewHome/', views.PruebaCreateViewHome.as_view(),
         name='PruebaCreateViewHome'),
    path('SuccesView/', views.SuccesView.as_view(), name='SuccesView'),
    path('', views.Home.as_view(), name='Home'),
]
