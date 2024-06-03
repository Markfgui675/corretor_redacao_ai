from corretor_ia.forms.login_user import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.http import Http404


def login_view(request):
    form = LoginForm()
    context = {
        'form':form,
        'text_button':'Entrar',
        'head_title':'RedAI - Entrar',
        'form_action':reverse('login-create')
    }
    return render(request, 'corretor_ia/login.html', context=context)

def login_create(request):
    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado')
            login(request, authenticated_user)
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Credenciais inválidas')
    return redirect(reverse('login-view'))

def my_account(request):
    context = {
        'head_title':'RedAI - conta'
    }
    return render(request, 'corretor_ia/account.html', context=context)
