from django.contrib import messages
from django.shortcuts import render, redirect
from sic_financeiro.usuarios.forms import UserModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from sic_financeiro.core.views.context_urls import context_urls as context_global


def signup(request):
    form = UserModelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                email_form = form.cleaned_data.get('email')
                existe_email = User.objects.filter(email=email_form).count()
                if existe_email > 0:
                    raise Exception('Esse email já foi cadastrado. Utilize outro.')

                request.POST['check_termo']
                form.save()
                messages.success(request, 'Usuário cadastrado com sucesso!')

                return redirect('/login')

            except Exception as e:
                messages.warning(request, e)
            except:
                messages.warning(request, 'Marque se concorda com os Termos')

        else:
            if form.errors['username']:
                messages.warning(request, form.errors['username'][0])

    context_global.context['form'] = form
    return render(request, '{0}/signup.html'.format(context_global.path_login), context_global.context)


def do_login(request):
    form = UserModelForm(request.POST or None)
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, 'Bem Vindo ao Sic Financeiro!')

            return redirect(context_global.url_home)

        else:
            messages.warning(request, 'Usuário ou senha não existente!')

    context_global.context['form'] = form
    return render(request, '{0}/login.html'.format(context_global.path_login), context_global.context)


@login_required
def do_logout(request):
    logout(request)
    messages.success(request, 'Saiu com Sucesso!')

    return redirect(context_global.url_login)


def termo(request):
    return render(request, '{0}/termo_de_uso.html'.format(context_global.path_login), context_global.context)
