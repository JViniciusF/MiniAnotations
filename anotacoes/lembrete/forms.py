
from django import forms
from .models import Lembrete

class Tlt_lembrete(forms.Form):
    titulo = forms.CharField(label='title_field', max_length=30)
    mensagem = forms.CharField(label= 'mnsg_field',max_length=200)
    Lembrete.titulo = titulo
    Lembrete.mensagem = mensagem

    