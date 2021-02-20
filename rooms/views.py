from django.views.generic import ListView
from django.shortcuts import render, redirect
from . import models

# Create your views here.


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 6
    ordering = "price"
    context_object_name = "rooms"


def room_detail(request, pk):
    return render(request, "rooms/detail.html")
