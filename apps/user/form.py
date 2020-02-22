from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import Customer



"""class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
"""




class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    # Here we add the extra form fields that we will use to create another model object
    phone = forms.CharField(required=False)
    dni = forms.CharField(required=False)
    
 
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        

        

"""class CustomerForm(UserCreationForm):
    
    class Meta:
        model = Customer
        fields = ['phone','dni','money']
        labels = {

            'phone':'Celular',
            'dni':'DNI',
            'money':'Saldo(S/.)'
        }
        widgets = {

            
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs = {'class': 'form-control'}),
            'money': forms.NumberInput(attrs= {'class': 'form-control'})
            
        }
      
"""

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