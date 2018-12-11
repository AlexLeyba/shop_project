from django import forms
from .models import Comment, Product


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class SellForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('date', 'user', 'article',)
