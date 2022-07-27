from django.contrib import admin
from produto.models import ProdutoComprado, AnunciarProduto, ImagemProduto

# Register your models here.

class ImagemProdutoAdmin(admin.StackedInline):
    model=ImagemProduto

@admin.register(AnunciarProduto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [ImagemProdutoAdmin]

    class Meta:
        model = AnunciarProduto


@admin.register(ImagemProduto)
class ProdutoImagemAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProdutoComprado)
