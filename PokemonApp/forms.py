from django import forms
from .models import Pokemon, PokemonType, Evaluation, Review

class EvaluationForm(forms.ModelForm):
    class Meta:
        model=Evaluation
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'