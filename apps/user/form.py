from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'dni', 'phone', 'money']
        labels = {
            'first_name': 'Nombres:',
            'last_name': 'Apellidos:',
            'dni': 'DNI:',
            'phone': 'Celular:',
            'money': 'Saldo (S/.)'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'id': 'id_first'
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'dni': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs= {
                    'class': 'form-control'
                }
            ),
            'money': forms.NumberInput(
                attrs= {
                    'class': 'form-control'
                }
            )
        }

