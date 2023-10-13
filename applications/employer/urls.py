from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "employer_app"

urlpatterns = [
    path('ListarTodosLosEmpleados',
         views.ListarTodosLosEmpleados.as_view(),
         name='ListarTodosLosEmpleados'
         ),
    path('AdministrarTodosLosEmpleados',
         views.AdministrarTodosLosEmpleados.as_view(),
         name='AdministrarTodosLosEmpleados'
         ),
    path('ActualizarEmpleado/<pk>/',
         views.ActualizarEmpleado.as_view(), name='ActualizarEmpleado'),
    path('EliminarEmpleado/<pk>/',
         views.EliminarEmpleado.as_view(), name='EliminarEmpleado'),
    path('CrearEmpleado',
         views.CrearEmpleado.as_view(), name='CrearEmpleado'),
    path('ListAllEmployerByDepartment', views.ListAllEmployerByArea.as_view()),
    path('ListarEmpleadosPorArea/<shortNameDepartment>',
         views.ListarEmpleadosPorArea.as_view(), name='ListarEmpleadosPorArea'),
    path('ListAllEmployerByAreaChar', views.ListAllEmployerByAreaChar.as_view()),
    path('ListAllEmployerByAreaChar2',
         views.ListAllEmployerByAreaChar2.as_view()),
    path('ListSkillsByEmploy', views.ListSkillsByEmploy.as_view()),
    path('EmployerDetailView/<pk>/', views.EmployerDetailView.as_view()),
    path('DetallesDelEmpleado/<pk>/',
         views.DetallesDelEmpleado.as_view(),
         name='DetallesDelEmpleado'),
    path('EmployerCreateView', views.EmployerCreateView.as_view()),
    path('EmployerCreateView2', views.EmployerCreateView2.as_view()),
    path('SuccesView', views.SuccesView.as_view(), name='SuccesView'),
    path('EmployerUpdate/<pk>/',
         views.EmployerUpdate.as_view(), name='EmployerUpdate'),
    path('EmployerDelete/<pk>/',
         views.EmployerDelete.as_view(), name='EmployerDelete'),
]
