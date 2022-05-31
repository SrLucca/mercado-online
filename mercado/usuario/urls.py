from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar', views.registrarUsuario, name="register"),
    path('login', views.loginUsuario, name="login"),
    path('logout', views.logoutUsuario, name="logout"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('configuracoes-profile', views.profileConfig, name="profile-configs"),

]