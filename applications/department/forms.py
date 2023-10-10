from django import forms


class NewDepartamentoForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    lastname = forms.CharField(max_length=50, required=False)
    nameDepartment = forms.CharField(max_length=50, required=False)
    shortNameDepartment = forms.CharField(max_length=5, required=False)
