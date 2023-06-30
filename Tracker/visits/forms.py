from django import forms
from .models import Visit
from .models import Clinic

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['doctor', 'date', 'notes']

class CreateClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'address', 'city', 'state', 'country']