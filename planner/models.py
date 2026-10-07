from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Snack", "Snack"),
        ("Dessert", "Dessert"),
    ]
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="Dinner")
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Minutes")

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    DAY_CHOICES = [(d, d) for d in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]]
    MEAL_CHOICES = [("Breakfast","Breakfast"),("Lunch","Lunch"),("Dinner","Dinner")]
    day = models.CharField(max_length=12, choices=DAY_CHOICES)
    meal_type = models.CharField(max_length=12, choices=MEAL_CHOICES)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("day", "meal_type")

    def __str__(self):
        return f"{self.day} - {self.meal_type}: {self.recipe.name}"
