from django import forms
from .models import Machine,Game

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'number', 'ip', 'start_time', 'end_time', 'user_id']
        labels = {
            'name': 'Nombre:',
            'number': 'Numero de maquina:',
            'ip': 'IP:',
            'start_time': 'Hora de inicio',
            'end_time': 'Hora de fin',
            'user_id': 'Usuario',
        }
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'number': forms.NumberInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'ip': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                }
            ),

            
        }
        

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'image', 'url']
        labels = {
            'name': 'Nombre:',
            'image': 'Imagen',
            'url': 'URL'
        }
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'image': forms.FileInput(

            ),
            'ip': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                }
            ),
        }