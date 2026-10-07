from django.shortcuts import get_object_or_404, redirect, render
from .forms import RecipeForm, MealPlanForm
from .models import Recipe, MealPlan

def home(request):
    return render(request, "home.html", {
        "recipe_count": Recipe.objects.count(),
        "plan_count": MealPlan.objects.count(),
    })

def recipe_list(request):
    recipes = Recipe.objects.all().order_by("name")
    return render(request, "recipe_list.html", {"recipes": recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe_detail.html", {"recipe": recipe})

def recipe_create(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("recipe_list")
    return render(request, "recipe_form.html", {"form": form, "title": "Add Recipe"})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect("recipe_detail", pk=pk)
    return render(request, "recipe_form.html", {"form": form, "title": "Edit Recipe"})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipe_list")
    return render(request, "recipe_confirm_delete.html", {"recipe": recipe})

def meal_plan(request):
    plans = MealPlan.objects.select_related("recipe").order_by("id")
    return render(request, "meal_plan.html", {"plans": plans})

def meal_plan_add(request):
    form = MealPlanForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("meal_plan")
    return render(request, "meal_plan_form.html", {"form": form})

def meal_plan_delete(request, pk):
    plan = get_object_or_404(MealPlan, pk=pk)
    if request.method == "POST":
        plan.delete()
        return redirect("meal_plan")
    return render(request, "meal_plan_confirm_delete.html", {"plan": plan})
