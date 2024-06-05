from corretor_ia.models import RedacaoComentario
from corretor_ia.forms.redacao import RedacaoForm
from corretor_ia.inteligencia.corretor import corretor_redacao
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required(login_url='login-view', redirect_field_name='next')
def redacaoAvaliacao(request, id):
    comentario = RedacaoComentario.objects.filter(id=id).first()
    context = {
        'head_title':'RedAI - avaliação de redação',
        'comentario':comentario
    }
    if comentario.avaliacoes.all().first() == request.user:
        return render(request, 'corretor_ia/corretor.html', context=context)
    else:
        return render(request, 'corretor_ia/index.html')

@login_required(login_url='login-view', redirect_field_name='next')
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