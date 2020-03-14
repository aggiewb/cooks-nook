from django.test import TestCase
from .models import Recipe, Review, User
from django.urls import reverse
from .views import index, veggieRecipeView, meatRecipeView, seafoodRecipeView, recipeDetails
from .forms import RecipeForm, ReviewForm

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
    
    def setUp(self):
        self.userRecipe = User.objects.create(username='Steven')
        self.recipe = Recipe.objects.create(name = 'Meatloaf', catagory = 'Meat', ingredients = ['Beef', 'Onion', 'Egg', 'Milk'], prep = 'Mix items together. Bake at 350 degrees for 45 minutes.', servings = 5, totalTime = 60, user = self.userRecipe)
        self.userReview = User.objects.create(username='Max')
        self.review = Review.objects.create(title = 'Family Friendly', rating = 'Great', comments='Quick and easy meal that I created in less than 30 min', recipe = self.recipe, user = self.userReview)
 
    def test_string_comment(self):
        reviewComment = self.review.comments
        self.assertEqual(str(reviewComment), 'Quick and easy meal that I created in less than 30 min')

    def test_string_rating(self):
        reviewRating = self.review.rating
        self.assertEqual(str(reviewRating), 'Great')

    def test_string_user(self):
        reviewUser = self.review.user
        self.assertEqual(str(reviewUser), 'Max')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class VeggieViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('veggie'))
        self.assertEqual(response.status_code, 200)

class MeatViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('meat'))
        self.assertEqual(response.status_code, 200)

class SeafoodViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('seafood'))
        self.assertEqual(response.status_code, 200)

class RecipeDetailsViewTest(TestCase):
    def setUp(self):
        self.userRecipe = User.objects.create(username='Steven')
        self.recipe = Recipe.objects.create(name = 'Meatloaf', catagory = 'Meat', ingredients = ['Beef', 'Onion', 'Egg', 'Milk'], prep = 'Mix items together. Bake at 350 degrees for 45 minutes.', servings = 5, totalTime = 60, user = self.userRecipe)
        self.userReview = User.objects.create(username='Max')
        self.review = Review.objects.create(title = 'Family Friendly', rating = 'Great', comments='Quick and easy meal that I created in less than 30 min', recipe = self.recipe, user = self.userReview)

    def test_meeting_details_success(self):
        response=self.client.get(reverse('recipeDetails', args=(self.recipe.id,)))
        self.assertEqual(response.status_code, 200)

class RecipeFormTest(TestCase):
    def setUp(self):
        self.userRecipe = User.objects.create(username='Steven')

    def test_typeform_is_valid(self):
        form=RecipeForm(data={'name': 'Meatloaf', 'catagory': 'Meat', 'ingredients': ['Beef', 'Onion', 'Egg', 'Milk'], 'prep': 'Mix items together. Bake at 350 degrees for 45 minutes.', 'servings': 5, 'totalTime': 60, 'user': self.userRecipe})
        self.assertTrue(form.is_valid())
    
    def test_typeform_empty(self):
        form=RecipeForm(data={'name': '', 'catagory': 'Meat', 'ingredients': [], 'prep': '', 'servings': None, 'totalTime': None, 'user': ''})
        self.assertFalse(form.is_valid())

class ReviewFormTest(TestCase):
    def setUp(self):
        self.userRecipe = User.objects.create(username='Steven')
        self.userReview = User.objects.create(username='Max')
        self.recipe = Recipe.objects.create(name = 'Meatloaf', catagory = 'Meat', ingredients = ['Beef', 'Onion', 'Egg', 'Milk'], prep = 'Mix items together. Bake at 350 degrees for 45 minutes.', servings = 5, totalTime = 60, user = self.userRecipe)

    def test_typeform_is_valid(self):
        form=ReviewForm(data={'title': 'Family Friendly', 'rating': 'Great', 'comments':'Quick and easy meal that I created in less than 30 min', 'recipe': self.recipe, 'user': self.userReview})
        self.assertTrue(form.is_valid())
    
    def test_typeform_empty(self):
        form=ReviewForm(data={'title': '', 'rating': '', 'comments':'', 'recipe': '', 'user': ''})
        self.assertFalse(form.is_valid())

class NewRecipeAuthenticationTest(TestCase):
    def setUp(self):
        self.testUser=User.objects.create_user(username='Susan', password='P@ssw0rd1')
        self.userRecipe = User.objects.create(username='Steven')
        self.recipe = Recipe.objects.create(name = 'Meatloaf', catagory = 'Meat', ingredients = ['Beef', 'Onion', 'Egg', 'Milk'], prep = 'Mix items together. Bake at 350 degrees for 45 minutes.', servings = 5, totalTime = 60, user = self.userRecipe)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('new_recipe'))
        self.assertRedirects(response, '/accounts/login/?next=/recipe/newrecipe/')

    def test_logged_in_uses_correct_template(self):
        login=self.client.login(username='Susan', password='P@ssw0rd1')
        response=self.client.get(reverse('new_recipe'))
        self.assertEqual(str(response.context['user']), 'Susan')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/new_recipe.html')
    
