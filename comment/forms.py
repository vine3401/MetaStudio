from django import forms
from .models import BlogComment, AppComment, SubBComment, SubAComment


class AppCommentForm(forms.ModelForm):
    class Meta:
        model = AppComment
        fields = ['text']


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['text']


class SubBCommentForm(forms.ModelForm):
    class Meta:
        model = SubBComment
        fields = ['text', 'user', 'toUser']


class SubACommentForm(forms.ModelForm):
    class Meta:
        model = SubAComment
        fields = ['text', 'user', 'toUser']