from django.shortcuts import render

from .models import Carro, Montadora

# Create your views here.
def index(request):
    montadoras = Montadora.objects.all()
    context = {
        'montadoras': montadoras,
    }
    return render(request, 'index.html', context)

def CarroDetail(request, pk):
    carro = Carro.objects.get(id=pk)
    montadora = carro.montadora

    context = {
        'carro': carro,
        'montadora': montadora
    }
    return render(request, 'carro-detalhes.html', context)

def MontadoraDetail(request, pk):
    montadora = Montadora.objects.get(id=pk)
    carro = montadora.carro_set.all()

    context = {
        'montadora': montadora,
        'carro': carro,
    }
    return render(request, 'carro-detalhes.html', context)