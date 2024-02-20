from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Página Inicial, bem vindo(a)!'
    context = {
	    "title": title,
	}
    return render(request, "index.html",context)
