from django.contrib import admin
from produto.models import ProdutoComprado, AnunciarProduto

# Register your models here.

admin.site.register(AnunciarProduto)
admin.site.register(ProdutoComprado)
