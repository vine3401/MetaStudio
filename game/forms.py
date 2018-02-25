from django import forms
from .models import Game, GameCategory

class UploadGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'version', 'inTro', 'category', 'author']