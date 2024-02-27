from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404, HttpResponseRedirect
from django.contrib.auth.models import User 
from .models import Produtos
from .forms import ProdutosFormCriar, FornecedorForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    # Obtém todos os usuários
    users = User.objects.all()
    
    # Obtém todos os produtos
    produtos = Produtos.objects.all()

    # Verifica se cada produto está com baixo estoque
    for produto in produtos:
        if produto.quantidade <= produto.alerta_estoque:
            produto.baixo_estoque = True
        else:
            produto.baixo_estoque = False

    # Define o título da página
    title = 'Página Inicial, bem vindo(a)!'

    # Cria o contexto para enviar para o template
    context = {
        "title": title,
        'users': users,
        'produtos': produtos,
    }

    # Renderiza a página index.html com o contexto fornecido
    return render(request, "index.html", context)

def listar_produto(request):
    title = 'Lista de Itens'
    produtos = Produtos.objects.all()
    context = {
        "title": title,
        "produtos": produtos,
    }
    return render(request, "listar_produto.html", context)


def adicionar_produto(request):
    form = ProdutosFormCriar(request.POST or None)
    if form.is_valid():
        form.save()
        # redirect to a success URL listar_produto
        return redirect('listar_produto')
    context = {
        "form": form,
    }
    return render(request, "adicionar_produto.html", context)
    
def list_supplier(request):
    context = {}

    fornecedores = FornecedorForm

    context['fornecedores'] = str(fornecedores)

    return render(request, "list_supplier.html", context)

def new_supplier(request):
    context ={}
 
    # create object of form
    form = FornecedorForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request, "new_supplier.html", context)

def editar_produto(request, id):
    context = {}
    produto = get_object_or_404(Produtos, id=id)
    form = ProdutosFormCriar(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('/listar_produto/')
    context["form"] = form
    return render(request, "editar_produto.html", context)

def apagar_produto(request, id):
    context={}
    produto = get_object_or_404(Produtos, id=id)
    if request.method == "POST":
        produto.delete()
        return redirect('/listar_produto/')
    context["produto"] = produto
    return render(request, "apagar_produto.html", context)


def register(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return render(request, 'register_success.html')  
    else:  
        form = UserCreationForm()  
    context = {  
        'form': form  
    }  
    return render(request, 'register.html', context)
