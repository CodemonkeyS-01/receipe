from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:receipe_id>", views.receipe, name="receipe")
]