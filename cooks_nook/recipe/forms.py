from django import forms
from .models import Recipe, Review

class RecipeForm(forms.ModelForm):
    totalTime = forms.CharField(label='Total Time (minutes)')
    class Meta:
        model=Recipe
        fields='__all__'