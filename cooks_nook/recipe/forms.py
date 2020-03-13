from django import forms
from .models import Recipe, Review

class RecipeForm(forms.ModelForm):
    totalTime = forms.CharField(label='Total Time (minutes)')
    catagory = forms.CharField(label='Category')
    class Meta:
        model=Recipe
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'