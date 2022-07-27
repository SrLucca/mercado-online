from django import forms
from .models import AnunciarProduto, ImagemProduto

class Anunciar(forms.ModelForm):


    class Meta:
        model = AnunciarProduto
        fields = ['nome','descricao','categoria', 'image']


class ImagensAnuncio(forms.ModelForm):
    
    class Meta:
        model = ImagemProduto
        fields = ['images']