from django.test import TestCase
from .models import Recipe, Review, User

class RecipeTest(TestCase):
    def test_string(self):
        recipe=Recipe(name='Fried Chicken')
        self.assertEqual(str(recipe), recipe.name)

    def test_table(self):
        self.assertEqual(str(Recipe._meta.db_table), 'recipe')
    
    def setUp(self):
        self.user=User.objects.create(username='Max')
        self.recipe = Recipe(name = 'Meatloaf', catagory = 'Meat', ingredients = ['Beef', 'Onion', 'Egg', 'Milk'], prep = 'Mix items together. Bake at 350 degrees for 45 minutes.', servings = 5, totalTime = 60, user = self.user)
    
    def test_string_prep(self):
        recipePrep=self.recipe.prep
        self.assertEqual(str(recipePrep), 'Mix items together. Bake at 350 degrees for 45 minutes.')
    
    def test_array_ingredients(self):
        recipeIngredients=self.recipe.ingredients
        self.assertEqual(recipeIngredients, ['Beef', 'Onion', 'Egg', 'Milk'])
    
    def test_string_catagory(self):
        recipeCatagory=self.recipe.catagory
        self.assertEqual(str(recipeCatagory), 'Meat')
    
    def test_num_servings_time(self):
        recipeServings = self.recipe.servings
        recipeTotalTime = self.recipe.totalTime
        self.assertEqual(recipeServings, 5)
        self.assertEqual(recipeTotalTime, 60)
    
    def test_user(self):
        recipeUser = self.recipe.user
        self.assertEqual(str(recipeUser), 'Max')

class ReviewTest(TestCase):
    def test_string(self):
        review=Review(title='Top Notch!')
        self.assertEqual(str(review), review.title)
        
    def test_table(self):
        self.assertEqual(str(Review._meta.db_table), 'review')

