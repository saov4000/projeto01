from django.shortcuts import render

def home(request):
    return render(request,'app/home.html',{})

def galeria(request):
    return render(request,'app/galeria.html',{})

def sobrenos(request):
    return render(request,'app/sobrenos.html',{})

def contato(request):
    return render(request,'app/contato.html',{})


