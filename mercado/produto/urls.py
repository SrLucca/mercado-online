from django.urls import path
from . import views

urlpatterns = [
    path('anunciar', views.userAnuncio, name="cadastro-anuncio"),
]