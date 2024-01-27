from .models import Music
from django import forms

class MusicForm(forms.ModelForm):
    class Meta:
        model=Music
        fields='__all__'