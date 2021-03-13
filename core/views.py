from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (Pessoa,
                     Veiculo,
                     MovRotativo,
                     Mensalista,
                     MovMensalista)

from .forms import PessoaForm

def home(request):
    context = {'mensagem' : 'Olá mundo'}
    return render(request, 'core/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

def pessoa_novo(request): ##url para quando usuario clicar no botao cadasrar
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def lista_veiculus(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos' : veiculos})

def lista_movrotativos(request):
    rotativos = MovRotativo.objects.all()
    return render(
        request,'core/lista_movrotativos.html', {'rotativos' : rotativos})

def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(
        request, 'core/lista_mensalistas.html', {'mensalistas' : mensalistas})

def lista_movmensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    return render(
        request, 'core/lista_movmensalistas.html', {'movmensalistas' : movmensalistas})