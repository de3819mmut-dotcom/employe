from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
# Como se quieren los empleados se debe importar el modelo
from .models import Employer
from .forms import EmpleadoForm
# Create your views here.

# Listar todos los empleados


# class ListarTodosLosEmpleados(ListView):
#     model = Employer
#     template_name = 'employer/Listar_Todos_Los_Empleados.html'
#     context_object_name = 'lista_empleados'

class ListarTodosLosEmpleados(ListView):
    template_name = 'employer/Listar_Todos_Los_Empleados.html'
    paginate_by = 2
    ordering = 'lastname'
    context_object_name = 'lista_empleados'
    model = Employer

    def get_queryset(self):
        palabraClave = self.request.GET.get('kword', '')
        listaEmpleados = Employer.objects.filter(
            lastname__icontains=palabraClave
        )
        print('listaEmpleados:', listaEmpleados)
        return listaEmpleados


class ListarEmpleadosPorArea(ListView):
    template_name = 'employer/ListarEmpleadosPorArea.html'
    context_object_name = 'lista_empleados_por_area'
    model = Employer
    # queryset = Employer.objects.filter(
    #     department__shortNameDepartment='C'
    # )

    def get_queryset(self):
        area = self.kwargs.get('shortNameDepartment')
        lista = Employer.objects.filter(

            department__shortNameDepartment=area
        )
        return lista


class AdministrarTodosLosEmpleados(ListView):
    template_name = 'employer/AdministrarTodosLosEmpleados.html'
    paginate_by = 2
    ordering = 'lastname'
    context_object_name = 'lista_empleados'
    model = Employer

    def get_queryset(self):
        palabraClave = self.request.GET.get('kword', '')
        listaEmpleados = Employer.objects.filter(
            lastname__icontains=palabraClave
        )
        print('listaEmpleados:', listaEmpleados)
        return listaEmpleados


class ActualizarEmpleado(UpdateView):
    template_name = "employer/ActualizarEmpleado.html"
    context_object_name = 'ActualizarEmpleado'
    model = Employer
    fields = [
        'name',
        'lastname',
        'job',
        'department',
        'skills',
    ]
    success_url = reverse_lazy('employer_app:AdministrarTodosLosEmpleados')


class EliminarEmpleado(DeleteView):
    model = Employer
    template_name = "employer/EliminarEmpleado.html"
    success_url = reverse_lazy('employer_app:AdministrarTodosLosEmpleados')


class CrearEmpleado(CreateView):
    model = Employer
    template_name = "employer/CrearEmpleado.html"
    # fields = ['name', 'lastname', 'job', 'department', 'cv','skills']
    # fields = ('__all__')
    form_class = EmpleadoForm
    # success_url = './SuccesView'
    success_url = reverse_lazy('employer_app:AdministrarTodosLosEmpleados')

    def form_valid(self, form):
        employer = form.save(commit=False)
        print(employer)
        employer.full_name = employer.name+' '+employer.lastname
        employer.save()
        return super(CrearEmpleado, self).form_valid(form)


class DetallesDelEmpleado(DetailView):
    model = Employer
    template_name = 'employer/DetallesDelEmpleado.html'
    context_object_name = 'employerDetailView'

    def get_context_data(self, **kwargs):
        context = super(DetallesDelEmpleado, self).get_context_data(**kwargs)
        context['skills'] = self.object.skills.all()
        context['titulo'] = 'Empleado del mes'
        return context

# Forma 1 Listar todos los empleados de un área de la empresa


class ListAllEmployerByArea(ListView):
    queryset = Employer.objects.filter(
        department__nameDepartment='Contabilidad'
    )
    template_name = 'employer/list_all_area.html'
    context_object_name = 'lista_empleados_area'
# Forma 2 Listar todos los empleados de un área de la empresa


# Listar todos los empleados por una palabra clave


class ListAllEmployerByAreaChar(ListView):
    def get_queryset(self):
        print('*********************')
        keyWord = self.request.GET.get('kword', '')
        print('keyWord:', keyWord)
        list = Employer.objects.filter(
            name=keyWord
        )
        print('list:', list)
        return list
    template_name = 'employer/list_all_areaChar.html'
    context_object_name = 'lista_empleados_areaChar'

# Listar todos los empleados por una palabra clave Paginación


class ListAllEmployerByAreaChar2(ListView):
    def get_queryset(self):
        keyWord = self.request.GET.get('kword2', '')
        print('keyWord:', keyWord)
        list = Employer.objects.filter(
            name=keyWord
        )
        print('list:', list)
        return list
    template_name = 'employer/list_all_areaChar2.html'
    paginate_by = 2
    context_object_name = 'lista_empleados_areaChar2'

# Listar habilidades de un empleado


class ListSkillsByEmploy(ListView):
    template_name = 'employer/listSkillsByEmploy.html'
    context_object_name = 'listSkillsByEmploy'

    def get_queryset(self):
        employ = Employer.objects.get(id=4)
        print(employ.skills.all())
        return employ.skills.all()

# Para usar la vista se debe activar la url


class EmployerDetailView(DetailView):
    model = Employer
    template_name = 'employer/employer_detail.html'
    context_object_name = 'employerDetailView'


class EmployerCreateView(CreateView):
    model = Employer
    template_name = "employer/employerCreateView.html"
    # fields = ['name', 'lastname', 'job', 'department', 'cv','skills']
    fields = ('__all__')
    success_url = './EmployerCreateView'


class SuccesView(TemplateView):
    template_name = "employer/successView.html"


class EmployerCreateView2(CreateView):
    model = Employer
    template_name = "employer/employerCreateView2.html"
    # fields = ['name', 'lastname', 'job', 'department', 'cv','skills']
    # fields = ('__all__')
    fields = ['name', 'lastname', 'job', 'department', 'cv', 'skills']
    # success_url = './SuccesView'
    success_url = reverse_lazy('employer_app:SuccesView')

    def form_valid(self, form):
        employer = form.save(commit=False)
        print(employer)
        employer.full_name = employer.name+' '+employer.lastname
        employer.save()
        return super(EmployerCreateView2, self).form_valid(form)


class EmployerUpdate(UpdateView):
    template_name = "employer/EmployerUpdate.html"
    model = Employer
    fields = [
        'name',
        'lastname',
        'job',
        'department',
        'skills',
    ]
    success_url = reverse_lazy('employer_app:SuccesView')


class EmployerDelete(DeleteView):
    model = Employer
    template_name = "employer/EmployerDelete.html"
    success_url = reverse_lazy('employer_app:SuccesView')
