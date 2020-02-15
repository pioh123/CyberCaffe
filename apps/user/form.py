from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
#from .models import User



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {
            'username':'Nombre de Usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Email'
        }




"""class UserForm(forms.ModelForm):
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
"""
class LoginAdminForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginAdminForm, self).__init__(*args, **kwargs)
        self.fields['username'].widgets.attrs['class'] = 'form-control'
        self.fields['username'].widgets.attrs['placeholder'] = 'Nombre del Usuario'
        self.fields['password'].widgets.attrs['class'] = 'form-control'
        self.fields['password'].widgets.attrs['placeholder'] = 'Contraseña'