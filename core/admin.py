from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "reservation_date", "reservation_time", "party_size", "status")
    list_filter = ("status", "reservation_date")
    search_fields = ("name", "email", "phone")
    ordering = ("reservation_date", "reservation_time")
