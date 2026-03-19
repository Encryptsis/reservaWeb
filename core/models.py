from django.db import models


class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pendiente"
        CONFIRMED = "confirmed", "Confirmada"
        CANCELLED = "cancelled", "Cancelada"

    name = models.CharField("nombre", max_length=120)
    email = models.EmailField("correo electrónico")
    phone = models.CharField("teléfono", max_length=30)
    party_size = models.PositiveSmallIntegerField("comensales")
    reservation_date = models.DateField("fecha")
    reservation_time = models.TimeField("hora")
    special_requests = models.TextField("peticiones especiales", blank=True)
    status = models.CharField(
        "estado",
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField("creada el", auto_now_add=True)

    class Meta:
        ordering = ["reservation_date", "reservation_time", "-created_at"]
        verbose_name = "reserva"
        verbose_name_plural = "reservas"

    def __str__(self) -> str:
        return f"{self.name} · {self.reservation_date} {self.reservation_time}"
