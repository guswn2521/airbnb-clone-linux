from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reservations)
class ReservationsAdmin(admin.ModelAdmin):

    """ Reservations Admin Definition """

    pass
