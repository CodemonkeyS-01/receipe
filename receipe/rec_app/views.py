from django.shortcuts import render
from . models import Receipes


# Create your views here.
def index(request):
    foods = Receipes.objects.all()
    return render(request, "rec_app/index.html",{
        "foods" :foods
    })

def receipe(request, receipe_id):
    receipe = Receipes.objects.get(id=receipe_id)
    return render(request, "rec_app/receipe.html",{
        "receipe": receipe
    })