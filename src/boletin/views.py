from django.shortcuts import render

from .forms import RegForm
# Create your views here.
def home(request):
    form = RegForm()
    context = {
        "form": form,
    }
    return render(request, "home.html", context)