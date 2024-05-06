from django.shortcuts import render
from .models import *

def inicio(request):
    return render(request,"home.html")

def gallery(request):
    return render(request,"components/galery.html")



"------------ Funciones de la API --------------"

def almuerzo(request):
    sandwiches = Sandwiches.objects.all()
    hamburguesas = Hamburguesas.objects.all()
    tapeos= Tapeo.objects.all()
    return render(request, "platos/almuerzo.html", 
                  {"sandwiches": sandwiches,
                  "hamburguesas": hamburguesas,
                  "tapeos":  tapeos})

def bebibas(request):
    bebidas = Bedidas.objects.all()
    tragos = Tragos.objects.all()
    return render(request, "platos/bebidas.html", 
                  {"bebidas": bebidas, 
                   "tragos": tragos})

def cafeteria(request):
    cafeteria = Cafeteria.objects.all()
    return render(request, "platos/cafes.html", 
                  {"cafeteria": cafeteria})

def ensalada(request):
    ensaladas = Ensaladas.objects.all()
    return render(request, "platos/ensalada.html", 
                  {"ensaladas": ensaladas})

def postres(request):
    postres = Postres.objects.all()
    return render(request, "platos/postres.html", 
                  {"postres": postres})

def desayuno(request):
    desayuno = Desayuno.objects.all()
    merienda = Merienda.objects.all()
    brusquetas = Brusquetas.objects.all()
    return render(request, "platos/desayuno.html", 
                  {"desayunos": desayuno, 
                   "meriendas":merienda,
                   "brusquetas":brusquetas
                   })
   