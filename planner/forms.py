from django import forms
from .models import Recipe, MealPlan

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "category", "ingredients", "instructions", "cooking_time"]
        widgets = {
            "ingredients": forms.Textarea(attrs={"rows": 5, "placeholder": "One ingredient per line"}),
            "instructions": forms.Textarea(attrs={"rows": 6, "placeholder": "Step-by-step instructions"}),
        }

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ["day", "meal_type", "recipe"]
