from django.shortcuts import render
from django.contrib.auth.models import User  
from .forms import FornecedorForm

# Create your views here.

def index(request):
    
    user = User.objects.all()
    
    title = 'Página Inicial, bem vindo(a)!'
    context = {
	    "title": title,
        'users': user,
	}
    return render(request, "index.html",context) 

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