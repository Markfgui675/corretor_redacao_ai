from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.shortcuts import redirect
from corretor_ia.forms.redacao import RedacaoForm
from corretor_ia.forms.create_user import RegisterForm
from corretor_ia.models import RedacaoComentario
from corretor_ia.inteligencia.corretor import corretor_redacao
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    context = {
        'index':True,
        'head_title':'RedAI - beta'
    }
    return render(request, 'corretor_ia/index.html', context=context)

def redacaoAvaliacao(request, id):
    comentario = RedacaoComentario.objects.filter(id=id).first()
    context = {
        'head_title':'RedAI - avaliação de redação',
        'comentario':comentario
    }
    return render(request, 'corretor_ia/corretor.html', context=context)

def corretor(request):
    redacao_form_data = request.session.get('redacao_form_data', None)
    form = RedacaoForm(redacao_form_data)
    context = {
        'head_title':'RedAI - Corretor',
        'form_action': reverse('send-redacao'),
        'form':form
    }
    return render(request, 'corretor_ia/corretor.html', context=context)

def sendRedacao(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['redacao_form_data'] = POST
    form = RedacaoForm(POST)
    redacao_id = 0

    if form.is_valid():
        redacao = form.save()
        comentario = corretor_redacao(redacao.redacao, request.user)
        redacao_id = comentario.id
        del(request.session['redacao_form_data'])

    return redirect('avaliacao-redacao', redacao_id)

def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    context = {
        'form':form,
        'text_button':'Criar conta',
        'head_title':'RedAI - Criar conta',
        'form_action':reverse('register-create')
    }

    return render(request, 'corretor_ia/create_user.html', context=context)

def register_create(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )
        login(request, authenticated_user)
        del(request.session['register_form_data'])
        return redirect(reverse('index'))
    else:
        messages.error(request, 'Não foi possível criar a conta')
        return redirect(reverse('register-view'))

def politica(request):
    context = {
        'head_title':'RedAI - Política de Privacidade'
    }
    return render(request, 'corretor_ia/politica.html', context=context)
