from django.db import models
# Create your models here.

class AnunciarProduto(models.Model):
    CATEGORIA = (
            ("Automóvel","Automóvel"),
            ("Eletrodoméstico","Eletrodoméstico"),
            ("Tecnologia","Tecnologia"),
            ("Alimento","Alimento"),
            ("Saúde","Saúde"),
            ("Vestuário","Vestuário"),
            ("Ferramenta","Ferramenta"),
        )

    nome = models.CharField(max_length=300, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)
    categoria = models.CharField(blank=False, null=False, choices=CATEGORIA, max_length=300)
    image = models.ImageField(blank=True)
    data_anuncio = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class ProdutoComprado(models.Model):
    produto = models.ManyToManyField(AnunciarProduto)

    def __str__(self):
        return self.produto

class ImagemProduto(models.Model):
    produto = models.ForeignKey(AnunciarProduto, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.produto.nome