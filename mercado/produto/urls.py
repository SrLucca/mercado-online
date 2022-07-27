from django.urls import path
from . import views

urlpatterns = [
    path('anunciar', views.userAnuncio, name="cadastro-anuncio"),
    path('produto/<int:id>', views.produtoView, name="info_produto"),
]