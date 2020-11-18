from django import forms

from .models import Suggestion

class AddSuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['name','email','subject','suggestion']
        