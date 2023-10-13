from django import forms

from .models import Employer


class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Employer
        fields = ('name', 'lastname', 'job',
                  'department', 'cv', 'avatar', 'fullname', 'skills',)
        widgets = {
            'skills': forms.CheckboxSelectMultiple()
        }
