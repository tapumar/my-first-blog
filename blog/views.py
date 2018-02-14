from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404,redirect, render_to_response
from .forms import PostForm, InscricaoForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Inscricao


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def sobre(request):
    return render(request, 'blog/sobre.html')

def contatos(request):
    return render(request, 'blog/contatos.html')

def amigos(request):
    return render(request, 'blog/amigos.html')

def servicos_list(request):
    return render(request, 'blog/servicos_list.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def encanadores(request):
    return render(request, 'services/encanador.html')


def eletricistas(request):
    return render(request, 'services/eletricista.html')

def pedreiros(request):
    return render(request, 'services/pedreiro.html')

def manicures(request):
    return render(request, 'services/manicure.html')

def cabelo(request):
    return render(request, 'services/cabelo.html')

def costura(request):
    return render(request, 'services/costura.html')

def jardinagem(request):
    return render(request, 'services/jardinagem.html')


def home(request):
        return render(request,'index.html')

def volta(request):
    return redirect('servicos')

class Criar(CreateView):
        template_name = 'services/cadastro.html'
        model = Inscricao
        success_url = reverse_lazy('servicos_list')
        fields = ('servico','nome', 'cpf', 'idade','email','telefone')

class Lista(ListView):
        template_name = 'services/lista.html'
        model = Inscricao
        context_object = 'nome'
