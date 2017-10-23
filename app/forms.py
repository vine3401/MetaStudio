from django import forms
from .models import App, AppCategory


class uploadAppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['']