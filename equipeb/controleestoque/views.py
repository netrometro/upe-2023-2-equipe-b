from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User 
from .models import Produtos, Fornecedor
from .forms import ProdutosFormCriar, FornecedorForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    user = User.objects.all()
    produtos = Produtos.objects.all()
    title = 'Página Inicial, bem vindo(a)!'
    context = {
        "title": title,
        'users': user,
    }
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

    fornecedores = Fornecedor.objects.all()

    context ['fornecedores'] = fornecedores

    return render(request, "list_supplier.html", context)

def update_supplier(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    fornecedor = get_object_or_404(Fornecedor, id = id)
 
    # pass the object as instance in form
    form = FornecedorForm(request.POST or None, instance = fornecedor)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/list_supplier')
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_supplier.html", context)

def new_supplier(request):
    context ={}
 
    # create object of form
    form = FornecedorForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return HttpResponseRedirect('/list_supplier')

    context['form']= form
    return render(request, "new_supplier.html", context)


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

def delete_supplier(request, id):
    context = {}
    fornecedor = get_object_or_404(Fornecedor, id=id)
    context["fornecedor"] = fornecedor

    if request.method == 'POST':
        fornecedor.delete()
        return HttpResponseRedirect('/list_supplier')
    return render(request, 'delete_supplier.html', context)