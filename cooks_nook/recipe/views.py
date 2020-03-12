from django.shortcuts import render
from .models import Recipe, Review

def index(request):
    return render(request, 'recipe/index.html')

def veggieRecipeView(request):
    veggieRecipeList=Recipe.objects.filter(catagory='Veggie')
    return render(request, 'recipe/veggie.html', {'veggieRecipeList': veggieRecipeList})

def meatRecipeView(request):
    meatRecipeList=Recipe.objects.filter(catagory='Meat')
    return render(request, 'recipe/meat.html', {'meatRecipeList': meatRecipeList})

def seafoodRecipeView(request):
    seafoodRecipeList=Recipe.objects.filter(catagory='Seafood')
    return render(request, 'recipe/seafood.html', {'seafoodRecipeList': seafoodRecipeList})

