from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from core.forms import ContatoForm
from core.models import Linguagens, Frameworks, Contato

# Create your views here.
def index(request):
    return render(request,"index.html")

def contato(request):
    if request.POST:
        form = ContatoForm(request.POST)
        
        if form.is_valid():
            #form.save()
            form.enviar()
    else:
        form = ContatoForm()
   
    contexto = {
        'contato' : form
    }
    return render(request, "contato.html", contexto)

def conhecimentos(request):
    contexto = {
        'Linguagens':Linguagens.objects.all(),
        'Frameworks': Frameworks.objects.all(),
         }
    return render(request,"conhecimentos.html", contexto)

