from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ReservationForm
from .models import Reservation


def home(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect(f"{reverse('home')}?created={reservation.pk}#reservar")
    else:
        form = ReservationForm()

    latest_reservation = Reservation.objects.order_by("-created_at").first()
    context = {
        "form": form,
        "total_reservations": Reservation.objects.count(),
        "latest_reservation": latest_reservation,
        "reservation_created": request.GET.get("created") is not None,
    }
    return render(request, "core/home.html", context)
