from django import forms
from django.core.exceptions import ValidationError

from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'photo', 'author', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'body': forms.Textarea(attrs={'class': 'textarea'}),
        }

# This function clears the input field after the call and checks the input field for the number of characters
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 150:
            raise ValidationError('Длина превышает 150 символов')

        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
