from django.shortcuts import render
from . models import Receipe


# Create your views here.
def index(request):
    foods = Receipe.objects.all()
    return render(request, "rec_app/index.html",{
        "foods" :foods
    })

def receipe(request, receipe_id):
    receipe = Receipe.objects.get(id=receipe_id)
    return render(request, "rec_app/receipe.html",{
        "receipe": receipe
    })