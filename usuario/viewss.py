import random
from builtins import print

from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView

from treecePythonDjango.models import Usuario
from .formsRecover import RecuperarUsuarioForm
from .forms import UserChangeForm
from .forms import InsereUsuarioForm


class IndexTemplateView(TemplateView):
    template_name = "nucleo/index.html"


class RecuperarView(TemplateView):

    def post(self, request, **kwargs):
        form = RecuperarUsuarioForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            usuario = Usuario.objects.filter(email=email)
            #
            if usuario.count() == 0:
                messages.error(request, 'Usuário não encontrado com o e-mail ' + email + '.')
                return render(request, 'usuario/recover.html', {'form': form})
            else:
                return sendmail(request, email, usuario, form)

    def get(self, request, **kwargs):
        form = RecuperarUsuarioForm()
        return render(request, 'usuario/recover.html', {'form': form})


class PostCreateView(TemplateView):

    def get(self, request, **kwargs):
        if kwargs.__len__() > 0 and kwargs['op'] == '1':
            return recuperarSenha(request)
        return render(request, 'usuario/cria.html', {'form': InsereUsuarioForm()})

    def post(self, request):
        form = InsereUsuarioForm(request.POST)
        if form.is_valid():
            usuario_email = form.cleaned_data['email']
            #
            usuarioAux = Usuario.objects.filter(email=usuario_email)
            if len(usuarioAux) == 0:
                #
                usuario_nome = form.cleaned_data['username']
                usuario_first_name = form.cleaned_data['first_name']
                usuario_last_name = form.cleaned_data['last_name']
                usuario_telefone = form.cleaned_data['telefone']
                usuario_celular = form.cleaned_data['celular']
                usuario_email = form.cleaned_data['email']
                usuario_estadoCivil = form.cleaned_data['estadoCivil']
                usuario_password = make_password(form.cleaned_data['password'])
                #
                usuario = Usuario(
                    username=usuario_nome,
                    first_name=usuario_first_name,
                    last_name=usuario_last_name,
                    email=usuario_email,
                    telefone=usuario_telefone,
                    celular=usuario_celular,
                    password=usuario_password,
                    estadoCivil=usuario_estadoCivil,
                )
                usuario.save()
                #
                messages.success(request, 'Usuário cadastrado com sucesso')
                return render(request, 'usuario/cria.html', {'form': InsereUsuarioForm()})
            else:
                messages.error(request, 'O e-mail "' + usuario_email + '" já foi utilizado em outra conta, favor '
                                                                       'informar outro endereço de e-mail.')
                return render(request, 'usuario/cria.html', {'form': InsereUsuarioForm()})
        else:
            messages.error(request, 'Nome de usuário já utilizado em outra conta, favor informar outro nome de '
                                    'usuário.')
            return render(request, 'usuario/cria.html', {'form': InsereUsuarioForm()})


class PostUpdateView(TemplateView):

    def post(self, request):
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save(commit=True)
            return redirect('nucleo:index')
        else:
            return redirect('nucleo:index')

    def get(self, request, **kwargs):
        usuario = Usuario.objects.get(id=request.user.id)
        form = InsereUsuarioForm(instance=usuario)
        return render(request, 'usuario/cria.html', {'form': form})


class UsuarioDeleteView(DeleteView):
    template_name = "usuario/exclui.html"
    model = Usuario
    context_object_name = 'usuario'
    success_url = reverse_lazy("nucleo:index")


def recuperarSenha(request, op=''):
    form = RecuperarUsuarioForm()
    return render(request, 'usuario/recover.html', {'form': form})


def sendmail(request, email, usuario, form):
    #
    number = random.randint(11111111, 99999999)
    usuario = usuario[0]
    usuario.randomNumber = number
    usuario.password = make_password(str(number))
    usuario.save()
    #
    send_mail('Treece Python Django',
              'Recuperação de senha. \n Sua nova senha temporarária é: ' + str(number) + '.'
              '\nVocê pode alterar a senha temporária no menu "Meu Perfil" após fazer login no sistema.',
              'abnergmb@live.com',
              [email],
              fail_silently=False, )
    #
    messages.success(request, 'E-mail de recuperação de senha enviado com sucesso.'
                              ' Favor verificar sua conta de email "' + email + '".')
    #
    return render(request, 'usuario/recover.html', {'form': form})
