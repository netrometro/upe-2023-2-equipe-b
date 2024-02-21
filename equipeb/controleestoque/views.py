from django.shortcuts import render
from django.contrib.auth.models import User 
from .models import Produtos
from .forms import ProdutosFormCriar

# Create your views here.

def index(request):
    
    user = User.objects.all()
    produtos = Produtos.objects.all()
    
    title = 'Página Inicial, bem vindo(a)!'
    context = {
	    "title": title,
        'users': user,
	}
    return render(request, "index.html",context) 

def listar_item(request):
	title = 'Lista de Itens'
	produtos = Produtos.objects.all()
	context = {
		"title": title,
		"produtos": produtos,
	}
	return render(request, "listar_item.html", context)

def adicionar_produto(request):
	form = ProdutosFormCriar(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		"form": form,
		"title": "Adicionar um produto",
	}
	return render(request, "listar_item.html", context)
