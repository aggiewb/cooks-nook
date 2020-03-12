from django.test import TestCase
from .models import Recipe, Review

class RecipeTest(TestCase):
    def test_string(self):
        recipe=Recipe(name='Fried Chicken')
        self.assertEqual(str(recipe), recipe.name)

    def test_table(self):
        self.assertEqual(str(Recipe.meta.db_table), 'recipe')
