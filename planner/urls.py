from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.recipe_list, name="recipe_list"),
    path("recipes/add/", views.recipe_create, name="recipe_create"),
    path("recipes/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("recipes/<int:pk>/edit/", views.recipe_edit, name="recipe_edit"),
    path("recipes/<int:pk>/delete/", views.recipe_delete, name="recipe_delete"),
    path("meal-plan/", views.meal_plan, name="meal_plan"),
    path("meal-plan/add/", views.meal_plan_add, name="meal_plan_add"),
    path("meal-plan/<int:pk>/delete/", views.meal_plan_delete, name="meal_plan_delete"),
]
