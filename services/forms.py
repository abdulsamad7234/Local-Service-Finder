from django import forms

from .models import Service


class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base_classes = (
            "w-full rounded-xl border border-slate-300 px-4 py-3 text-slate-800 "
            "outline-none transition placeholder:text-slate-400 "
            "focus:border-brand-500 focus:ring-4 focus:ring-brand-100"
        )
        placeholders = {
            "title": "Ex: Home Plumbing Repair",
            "provider_name": "Ex: XYZ Services",
            "city": "Ex: Gorakhpur",
            "phone": "Ex: 03001234567",
            "email": "Ex: provider@example.com",
            "address": "Ex: Golghar Town, Block B",
            "description": "Describe the service, experience, and what customers can expect.",
        }
        for name, field in self.fields.items():
            field.widget.attrs["class"] = base_classes
            field.widget.attrs["placeholder"] = placeholders.get(name, "")

    class Meta:
        model = Service
        fields = [
            "title",
            "provider_name",
            "category",
            "city",
            "phone",
            "email",
            "address",
            "description",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        digits = [char for char in phone if char.isdigit()]
        if len(digits) < 10:
            raise forms.ValidationError("Enter a valid phone number with at least 10 digits.")
        return phone
