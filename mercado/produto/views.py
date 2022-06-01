from django.shortcuts import render, get_object_or_404, redirect
from django.http import QueryDict
from .forms import Anunciar
from usuario.models import Profile
from produto.models import AnunciarProduto
from django.contrib import messages
# Create your views here.

def userAnuncio(request):
    usuario = Profile.objects.filter(user=request.user)
    if request.method == 'POST':
        form = Anunciar(request.POST)
        nome_cadastro = QueryDict.get(request.POST, key='nome')
        descricao_cadastro = QueryDict.get(request.POST, key='descricao')
        categoria_cadastro = QueryDict.get(request.POST, key='categoria')
        imagens_cadastro = QueryDict.getlist(request.FILES, key='image')
        print(imagens_cadastro)

        if form.is_valid():
            for img in imagens_cadastro:
                anuncio = AnunciarProduto.objects.create(nome=nome_cadastro, descricao=descricao_cadastro, categoria=img)
            anuncio.save()
            for objetos in usuario:
                objetos.produto_anunciado.add(anuncio)
                objetos.save()
            messages.success(request, "Cadastro Concluído!")
            return redirect(f"/profile/{request.user.username}")
        else:
            messages.error(request, "Erro no cadastro. Informação Inválida")
    form = Anunciar()

    return render(request, 'anunciar/cadastro.html', {"form":form})
