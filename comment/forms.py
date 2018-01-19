from django import forms
from .models import BlogComment, GameComment, SubBComment, SubGComment


class GameCommentForm(forms.ModelForm):
    class Meta:
        model = GameComment
        fields = ['text']


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['text']


class SubBCommentForm(forms.ModelForm):
    class Meta:
        model = SubBComment
        fields = ['text', 'user', 'toUser']


class SubGCommentForm(forms.ModelForm):
    class Meta:
        model = SubGComment
        fields = ['text', 'user', 'toUser']