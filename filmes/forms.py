from django import forms 
from .models import Genero, Filme

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
