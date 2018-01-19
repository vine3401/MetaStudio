from django import forms
from .models import App, AppCategory


class UploadAppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['name', 'version', 'inTro', 'category', 'author']