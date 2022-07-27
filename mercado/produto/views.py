from django.shortcuts import render, get_object_or_404, redirect
from django.http import QueryDict
from .forms import Anunciar, ImagensAnuncio
from usuario.models import Profile
from produto.models import AnunciarProduto, ImagemProduto
from django.contrib import messages
# Create your views here.

def userAnuncio(request):
    usuario = Profile.objects.filter(user=request.user)
    if request.method == 'POST':
        form1 = Anunciar(request.POST)
        form2 = ImagensAnuncio(request.FILES)
        nome_cadastro = QueryDict.get(request.POST, key='nome')
        descricao_cadastro = QueryDict.get(request.POST, key='descricao')
        categoria_cadastro = QueryDict.get(request.POST, key='categoria')
        imagens_cadastro = QueryDict.get(request.FILES, key='image')
        print(imagens_cadastro)

        if form1.is_valid() and form2.is_valid():
            anuncio = AnunciarProduto.objects.create(nome=nome_cadastro, descricao=descricao_cadastro, categoria=categoria_cadastro, image=imagens_cadastro)
            anuncio.save()
            imagens = ImagemProduto.objects.create(produto=anuncio, images=form2)
            for objetos in usuario:
                objetos.produto_anunciado.add(anuncio)
                objetos.save()
            messages.success(request, "Cadastro Concluído!")
            return redirect(f"/profile/{request.user.username}")
        else:
            messages.error(request, "Erro no cadastro. Informação Inválida")
    form1 = Anunciar()
    form2 = ImagensAnuncio()

    return render(request, 'anunciar/cadastro.html', {"form1":form1,"form2":form2})

def produtoView(request, id):

    produto = get_object_or_404(AnunciarProduto, pk=id)
    imagens = ImagemProduto.objects.filter(produto=produto)

    return render(request, 'produto_templates/produto.html', {'produto_objs':produto, 'imagem_produto':imagens})