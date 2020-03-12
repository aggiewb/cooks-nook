from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('veggie/', views.veggieRecipeView, name='veggie'),
    path('meat/', views.meatRecipeView, name='meat'),
    path('seafood', views.seafoodRecipeView, name='seafood'),
    path('details/<int:id>', views.recipeDetails, name='recipeDetails'),
]