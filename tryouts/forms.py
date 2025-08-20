# forms.py
from django import forms
from .models import TryoutRegistrant, TryoutEvent
from django.utils import timezone

class TryoutRegistrantForm(forms.ModelForm):
    tryout_event = forms.ModelChoiceField(
        queryset = TryoutEvent.objects.all().order_by('date'),
        empty_label="Select a tryout event",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = TryoutRegistrant
        fields = [
            "tryout_event",
            "first_name",
            "last_name",
            "email",
            "phone",
            "weight_class",
            "experience_years",
            "image",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "weight_class": forms.TextInput(attrs={"class": "form-control", "placeholder": "Weight Class"}),
            "experience_years": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Years of Experience"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }
