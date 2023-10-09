from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "employer_app"

urlpatterns = [
    path('ListAllEmployer', views.ListAllEmployer.as_view()),
    path('ListAllEmployerByDepartment', views.ListAllEmployerByArea.as_view()),
    path('ListAllEmployerByDepartment2/<shortName>', views.ListAllEmployerByArea2.as_view()),
    path('ListAllEmployerByAreaChar', views.ListAllEmployerByAreaChar.as_view()),
    path('ListAllEmployerByAreaChar2', views.ListAllEmployerByAreaChar2.as_view()),
    path('ListSkillsByEmploy', views.ListSkillsByEmploy.as_view()),
    path('EmployerDetailView/<pk>/', views.EmployerDetailView.as_view()),
    path('EmployerDetailView2/<pk>/', views.EmployerDetailView2.as_view()),
    path('EmployerCreateView', views.EmployerCreateView.as_view()),
    path('EmployerCreateView2', views.EmployerCreateView2.as_view()),
    path('SuccesView', views.SuccesView.as_view(), name='SuccesView'),
]