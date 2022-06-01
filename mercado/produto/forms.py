from django import forms
from .models import AnunciarProduto

class Anunciar(forms.ModelForm):

    class Meta:
        model = AnunciarProduto
        fields = ['nome','descricao','categoria']