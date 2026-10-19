from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields=['rut', 'nombre', 'apellido', 'email', 'telefono', 'foto']
        widgets={
            'rut':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej: 12345678-9'}),
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej: Nombre'}),
            'apellido':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej: Apellido'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej: correo@ejemplo.com'}),
            'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej: +56912345678'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
        }
        labels = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo electrónico', 
            'telefono': 'Telefono',
            'foto': 'Foto',
        }