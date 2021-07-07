from django import forms
from django.db.models import fields
from .models import Subscribe


class EmailSubscribeForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "id": "email",
        "class":  "form-control form-control-lg",
        "name": "email",
        "placeholder": "Email Address",
    }), label="")

    class Meta:
        model = Subscribe
        fields = ('email', )
