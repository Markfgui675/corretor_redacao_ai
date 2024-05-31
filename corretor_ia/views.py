from django.shortcuts import render

def index(request):
    context = {
        'head_title':'RedAI - beta'
    }
    return render(request, 'corretor_ia/index.html', context=context)

def corretor(request):
    context = {
        'head_title':'RedAI - Corretor'
    }
    return render(request, 'corretor_ia/corretor.html', context=context)

def politica(request):
    context = {
        'head_title':'RedAI - Política de Privacidade'
    }
    return render(request, 'corretor_ia/politica.html', context=context)
