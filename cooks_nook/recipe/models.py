from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Recipe(models.Model):
    MEAT = 'Meat'
    SEAFOOD = 'Seafood'
    VEGGIE = 'Veggie'
    CATAGORY_CHOICES=[
        (MEAT, 'Meat'),
        (SEAFOOD, 'Seafood'),
        (VEGGIE, 'Veggie'),
    ]

    name = models.CharField(max_length=60)
    catagory = models.CharField(max_length=7, choices=CATAGORY_CHOICES, default=MEAT)
    ingredients = ArrayField(models.CharField(max_length=20))
    prep = models.TextField()
    servings = models.SmallIntegerField()
    totalTime = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'recipe'
        verbose_name = 'recipes'

class Review(models.Model):
    GREAT = 'Great'
    AVERAGE = 'Average'
    POOR = 'Poor'
    RATING_CHOICES = [
        (GREAT, 'Great'),
        (AVERAGE, 'Average'),
        (POOR, 'Poor'),
    ]
    
    title = models.CharField(max_length=60)
    rating=models.CharField(max_length=7, choices=RATING_CHOICES, default=GREAT)
    comments=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'review'
        verbose_name = 'reviews'
