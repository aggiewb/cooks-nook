from django.test import TestCase
from .models import Recipe, Review

class RecipeTest(TestCase):
    def test_string(self):
        recipe=Recipe(name='Fried Chicken')
        self.assertEqual(str(recipe), recipe.name)

    def test_table(self):
        self.assertEqual(str(Recipe._meta.db_table), 'recipe')

class ReviewTest(TestCase):
     def test_string(self):
        review=Review(name='Top Notch!')
        self.assertEqual(str(review), review.name)

    def test_table(self):
        self.assertEqual(str(Review._meta.db_table), 'review')

