from django.shortcuts import render
from . models import Receipes, Container


# Create your views here.
def index(request):
    foods = Receipes.objects.all()
    return render(request, "rec_app/index.html",{
        "foods" :foods
    })

def receipe(request, receipe_id):
    receipe = Receipes.objects.get(id=receipe_id)
    containers = receipe.container.all()
    
    return render(request, "rec_app/receipe.html",{
        "receipe": receipe,
        "containers": containers,
    })