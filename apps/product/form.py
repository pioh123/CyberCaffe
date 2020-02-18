from django import forms
from .models import Product, Advertise,Promotion

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'photo', 'stock', 'price']
        labels = {
            'name': 'Nombre:',
            'photo': 'Foto:',
            'stock': 'Stock:',
            'price': 'Precio (S/.)',
        }
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'id': 'id_first'
                }
            ),
            'photo': forms.FileInput(

            ),
            'stock': forms.NumberInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs= {
                    'class': 'form-control',
                    'step': "0.01"
                }
            ),
            
        }

class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertise
        fields = ['name','image','description','typea']
        labels = {
            'name': 'Nombre',
            'image': 'Imagen',
            'description': 'Descripción',
            'typea': 'Tipo'
        }
        widgets = {
            'name': forms.TextInput(
                attrs= {
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(),
            'description': forms.Textarea(),
            'typea': forms.HiddenInput()
        }

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['name','image']
        labels = {
            'name': 'Nombre',
            'image': 'Imagen',
            
        }
        widgets = {
            'name': forms.TextInput(
                attrs= {
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(),
            
        }
       