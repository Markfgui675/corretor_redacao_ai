from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.shortcuts import redirect
from corretor_ia.forms.redacao import RedacaoForm
from corretor_ia.models import RedacaoComentario
from corretor_ia.inteligencia.corretor import corretor_redacao

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
        comentario = corretor_redacao(redacao.redacao)
        redacao_id = comentario.id
        del(request.session['redacao_form_data'])

    return redirect('avaliacao-redacao', redacao_id)

def politica(request):
    context = {
        'head_title':'RedAI - Política de Privacidade'
    }
    return render(request, 'corretor_ia/politica.html', context=context)
