from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, verbose_name="nombre")),
                ("email", models.EmailField(max_length=254, verbose_name="correo electrónico")),
                ("phone", models.CharField(max_length=30, verbose_name="teléfono")),
                ("party_size", models.PositiveSmallIntegerField(verbose_name="comensales")),
                ("reservation_date", models.DateField(verbose_name="fecha")),
                ("reservation_time", models.TimeField(verbose_name="hora")),
                ("special_requests", models.TextField(blank=True, verbose_name="peticiones especiales")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pendiente"),
                            ("confirmed", "Confirmada"),
                            ("cancelled", "Cancelada"),
                        ],
                        default="pending",
                        max_length=20,
                        verbose_name="estado",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="creada el")),
            ],
            options={
                "verbose_name": "reserva",
                "verbose_name_plural": "reservas",
                "ordering": ["reservation_date", "reservation_time", "-created_at"],
            },
        ),
    ]
