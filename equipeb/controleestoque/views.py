from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    
    user = User.objects.all()
    
    title = 'Página Inicial, bem vindo(a)!'
    context = {
	    "title": title,
        'users': user,
	}
    return render(request, "index.html",context) 



def register(request):  
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()  
        messages.success(request, 'Account created successfully')  
  
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context)  