import os
import re
from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'email', 'telefono', 'foto']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-5'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ej: correo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: +56912345678'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'foto': 'Foto',
        }

    def clean_rut(self):
        rut = self.cleaned_data['rut'].replace('.', '').strip().upper()
        if not re.match(r'^\d{7,8}-[\dK]$', rut):
            raise forms.ValidationError('El RUT debe tener el formato 12345678-5.')
        numero, dv = rut.split('-')
        suma = 0
        multiplicador = 2
        for digito in reversed(numero):
            suma += int(digito) * multiplicador
            multiplicador = multiplicador + 1 if multiplicador < 7 else 2
        resto = 11 - (suma % 11)
        if resto == 11:
            dv_esperado = '0'
        elif resto == 10:
            dv_esperado = 'K'
        else:
            dv_esperado = str(resto)
        if dv != dv_esperado:
            raise forms.ValidationError('El RUT no es válido: el dígito verificador no coincide.')
        return rut

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono'].replace(' ', '')
        if not re.match(r'^\+?\d{8,12}$', telefono):
            raise forms.ValidationError('El teléfono debe tener solo números (8 a 12 dígitos).')
        return telefono

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto:
            extension = os.path.splitext(foto.name)[1].lower()
            if extension not in ['.jpg', '.jpeg', '.png']:
                raise forms.ValidationError('La foto debe ser un archivo JPG o PNG.')
        return foto