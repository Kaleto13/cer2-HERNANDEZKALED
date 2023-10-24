from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User
from miapp.models import *
from miapp.forms import *
# Create your views here.



def index(request):
    title = "Inicio"
    entidad = Entidades.objects.all()
    data = {
        "title": title,
    }

    return render(request,'miapp/index.html', {"entidades": entidad})

def carreras(request):
    comunicado = Comunicado.objects.order_by('fecha_publicacion').all()
    entidades = Entidades.objects.all()
    data = {
        'entidades': entidades,
        'comunicados': comunicado,
    }
    
    return render(request,'miapp/carreras.html', data)

#Funciones sin utilizar (me dio flojera borrarlo) :P
def crear(request):
    formulario = Comunicado_form(request.POST or None)
    
    print("GUARDADOOOO")
    if formulario.is_valid():
        formulario.save()
        print("FORMULARIO VALIDOOOOOOOOOOO")
        return redirect('carreras')
    return render(request, 'miapp/crear.html', {"formulario":formulario})

def editar(request, id):
    comunicado = Comunicado.objects.get(id=id)
    formulario = Comunicado_form(request.POST or None, request.FILES or None, instance=comunicado)
    if formulario.is_valid():
        print("FORMULARIO VALIDOOOOOOOOOOO")
        formulario.save()
        return redirect(carreras)
    return render(request,'miapp/editar.html',{"formulario":formulario})