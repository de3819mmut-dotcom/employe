from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
# Create your views here.
from .forms import NewDepartamentoForm
from applications.employer.models import Employer
from .models import Department


class ListarDepartamentos(ListView):
    model = Department
    template_name = "department/ListarDepartamentos.html"
    context_object_name = 'lista_empleados_departamento'


class CrearDepartamento(FormView):
    template_name = 'department/CrearDepartamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        departamento = Department(
            nameDepartment=form.cleaned_data['nameDepartment'],
            shortNameDepartment=form.cleaned_data['shortNameDepartment'],
        )
        departamento.save()
        nameF = form.cleaned_data['name']
        lastnameF = form.cleaned_data['lastname']
        Employer.objects.create(
            name=nameF,
            lastname=lastnameF,
            job='1',
            department=departamento
        )
        return super(CrearDepartamento, self).form_valid(form)


class IndexView(TemplateView):
    template_name = 'index.html'


class NewDepartamentoView(FormView):
    template_name = 'department/new_deparments.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        departamento = Department(
            nameDepartment=form.cleaned_data['nameDepartment'],
            shortNameDepartment=form.cleaned_data['shortNameDepartment'],
        )
        departamento.save()
        nameF = form.cleaned_data['name']
        lastnameF = form.cleaned_data['lastname']
        Employer.objects.create(
            name=nameF,
            lastname=lastnameF,
            job='1',
            department=departamento
        )
        return super(NewDepartamentoView, self).form_valid(form)
