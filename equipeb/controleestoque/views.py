from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User 
from .models import Produtos, Fornecedor
from .forms import ProdutosFormCriar, FornecedorForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import tempfile
from django.template.loader import render_to_string
import weasyprint
from datetime import datetime

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

def delete_supplier(request, id):
    context = {}
    fornecedor = get_object_or_404(Fornecedor, id=id)
    context["fornecedor"] = fornecedor

    if request.method == 'POST':
        fornecedor.delete()
        return HttpResponseRedirect('/list_supplier')
    return render(request, 'delete_supplier.html', context)

def generate_qrCode(request, number):
    context = {}
    wa_endPoint = f'https://wa.me/{number}'
    api_url = f'https://quickchart.io/qr?text={wa_endPoint}'
    response = requests.get(api_url)
    if response.status_code == 200:
        qr_code_url = response.url
        context['url'] = qr_code_url
        return render(request, 'qr_code.html', context)  # Return JSON response to the client
    else:
        # If the request was not successful, handle the error accordingly
        # For example, you can return an error message or render an error template
        error_message = f"Failed to fetch data from API. Status code: {response.status_code}"
        return render(request, 'error_template.html', {'error_message': error_message})

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()

def bar_produtos_chart(request):
    labels = []
    data = []

    queryset = Produtos.objects.values('nome').annotate(quantidade=Sum('quantidade'))
    for produto in queryset:
        labels.append(produto['nome'])  # Alteração aqui: corrigir a atribuição do nome do produto
        data.append(produto['quantidade'])

    return JsonResponse({
        'labels': labels,
        'data': data,
    })
# EOF

def export_pdf (request):
	products = Produtos.object.all()
	
	html_index = render_to_string('export-pdf.html', {'products':products})
	
	weasyprint_html = weasyprint.HTML(string=html_index, base_url='http://127.0.0.1:8000/media')
	pdf = weasyprint_html.write_pdf(stylesheets=[weasyprint.CSS(string='body { font-family: serif} img {margin: 10px; width: 50px;}')])
	
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=Products'+str(datetime.datetime.now())+'.pdf'
	response[ 'Content-Transfer-Encoding'] = 'binary'
	
	with tempfile.NamedTemporaryFile(delete=True) as output:
		output.write(pdf)
		output.flush()
		output.seek(0)
		response.write(output.readread())
	return response
