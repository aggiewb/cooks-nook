from django.shortcuts import render, get_object_or_404
from .models import Recipe, Review, User

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

def recipeDetails(request, id):
    recipe=get_object_or_404(Recipe, pk=id)
    reviews=Review.objects.filter(recipe=id)
    context={
        'recipe': recipe,
        'reviews': reviews,
    }
    return render(request, 'recipe/details.html', context=context)