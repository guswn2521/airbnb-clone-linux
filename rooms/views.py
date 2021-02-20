from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=6)
    rooms = paginator.page(int(page))
    # print(rooms.object_list)
    return render(
        request,
        "rooms/home.html",
        context={"page": rooms},
    )
