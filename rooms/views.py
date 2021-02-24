from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models

# Create your views here.


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 6
    ordering = "price"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ Room Detail Definition """

    model = models.Room


def search(request):
    print(request.GET)
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        context={"city": city, "countries": countries, "room_types": room_types},
    )
