from django.conf import settings
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.
def home(request):
    titulo = "HOLA"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    
    context = {
        "titulo": titulo,
        "form": form,
        }
    
    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "PERSONA"
        instance.save()
        
        context = {
            "titulo": "Gracias %s!" %(nombre)
        }

        if not nombre:
            context = {
                "titulo": "Gracias %s!" %(email)
            }

        print (instance)
        print (instance.timestamp)


    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key in form.cleaned_data:
            print (key)
            print (form.cleaned_data.get(key))

    context = {
        "form": form,
    }
    return render(request, "forms.html", context)