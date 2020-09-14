from django.shortcuts import render
from django.forms import forms
from .models import Lembrete
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

from .forms import Tlt_lembrete

# Create your views here.

def home (request):
    lembretes = Lembrete.objects.all()
    return render(request,'home.html',{'lembretes':lembretes})

def add(request):
    lbt_titulo = request.POST["lbt_titulo"]
    lbt_msg = request.POST["lbt_msg"]

    n_lembrete = Lembrete(titulo=lbt_titulo,mensagem = lbt_msg)

    n_lembrete.save()
    lembretes = Lembrete.objects.all()
    return redirect(home)

def delete(request,id):
    lembreteDel = Lembrete.objects.filter(id = id)
    lembreteDel.delete()
    lembretes = Lembrete.objects.all()
    home(request)
    return redirect(home)