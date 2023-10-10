from django import forms

from .models import Prueba
from datetime import date, datetime
class PruebaForm(forms.ModelForm):

  class Meta:
    model = Prueba
    #fields = ('__all__')
    fields = ('nombre','apellido','edad','fecha_nacimiento')
    widgets = {
      'nombre': forms.TextInput(
        attrs = {
          'placeholder':'Escriba su nombre',
          'class':'Nombre'
        }
      ),
      'apellido':forms.TextInput(),
      'edad':forms.NumberInput(),
      'fecha_nacimiento' : forms.DateInput(attrs={'type': 'date'})
    }
  def clean_edad(self):
    edad = self.cleaned_data.get('edad')
    if edad < 18:
      raise forms.ValidationError('Edad mayor a 18')
    return edad
