from django.shortcuts import render
from django.http import HttpResponse

from .models import Pessoa
# Create your views here.

def index(request):

    return render(request,'index.html')

def list_pessoas(request):
    pessoa = Pessoa.objects.all()
    contexto = {'pessoas':pessoa}

    return render(request,'index.html',contexto)
