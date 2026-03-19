from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    reservation_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Fecha",
    )
    reservation_time = forms.TimeField(
        widget=forms.TimeInput(attrs={"type": "time"}),
        label="Hora",
    )
    special_requests = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label="Peticiones especiales",
    )

    class Meta:
        model = Reservation
        fields = [
            "name",
            "email",
            "phone",
            "party_size",
            "reservation_date",
            "reservation_time",
            "special_requests",
        ]
        labels = {
            "name": "Nombre",
            "email": "Correo electrónico",
            "phone": "Teléfono",
            "party_size": "Comensales",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ana García"}),
            "email": forms.EmailInput(attrs={"placeholder": "ana@email.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+34 600 123 456"}),
            "party_size": forms.Select(
                choices=[(2, "2 personas"), (4, "4 personas"), (6, "6 personas"), (8, "8 personas")]
            ),
            "special_requests": forms.Textarea(
                attrs={"placeholder": "Alergias, celebración, terraza o silla para bebé"}
            ),
        }

    def clean_party_size(self):
        party_size = self.cleaned_data["party_size"]
        if party_size < 1:
            raise forms.ValidationError("Selecciona al menos un comensal.")
        return party_size
