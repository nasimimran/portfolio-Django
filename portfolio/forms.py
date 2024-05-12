from django import forms
from .models import Contacted


class ContactedForm(forms.ModelForm):
    class Meta:
        model = Contacted
        fields = "__all__"
