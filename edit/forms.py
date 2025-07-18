from django import forms
from data.models import Sources, Quotes

class SourceForm(forms.ModelForm):
    class Meta:
        model = Sources
        fields = ['source']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quotes
        fields = ['quote', 'weight',]
