from django import forms
from django.contrib.auth.models import User
from .models import Post, Inscricao


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class InscricaoForm(forms.ModelForm):

        class Meta:
                model = Inscricao
                fields = ('servico','nome', 'cpf', 'idade','email','telefone')
