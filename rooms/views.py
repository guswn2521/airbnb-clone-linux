from django.views.generic import ListView, DetailView
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
