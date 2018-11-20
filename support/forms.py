from django import forms
from .models import Help


class SupForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = ('email',
                  'title',
                  'text')
