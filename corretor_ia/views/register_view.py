from corretor_ia.forms.create_user import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.http import Http404


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