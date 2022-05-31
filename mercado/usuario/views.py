from django.shortcuts import  render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import NewUser
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.

def registrarUsuario(request):
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Concluído!")
            print("deu certo")
            return redirect("/")
        else:
            messages.error(request, "Erro no cadastro. Informação Inválida")

            print("deu errado")
    form = NewUser()
    
    return render(request, 'register/register.html', {'register_form':form})

def loginUsuario(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Você está agora logado {username}.")
                return redirect("/")
            else:
                messages.error(request, "Nome de usuário ou senha inválidos!")
        else:
            messages.error(request, "Nome de usuário ou senha inválidos!")
    form = AuthenticationForm()

    return render(request, 'login/login.html', {"login_form":form})

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request, username):
    
    user_request = get_object_or_404(User, username=username)
    
    return render(request, 'profile/profile.html', {'user_request':user_request})

def profileConfig(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Sua conta foi atualizada!')
            return redirect('/profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile/alterar_profile.html', context)