from django.shortcuts import render
from django.contrib.auth.models import User  

# Create your views here.

def index(request):
    
    user = User.objects.all()
    
    title = 'Página Inicial, bem vindo(a)!'
    context = {
	    "title": title,
        'users': user,
	}
    return render(request, "index.html",context) 
