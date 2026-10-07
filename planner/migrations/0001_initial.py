from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("category", models.CharField(choices=[("Breakfast","Breakfast"),("Lunch","Lunch"),("Dinner","Dinner"),("Snack","Snack"),("Dessert","Dessert")], default="Dinner", max_length=30)),
                ("ingredients", models.TextField()),
                ("instructions", models.TextField()),
                ("cooking_time", models.PositiveIntegerField(help_text="Minutes")),
            ],
        ),
        migrations.CreateModel(
            name="MealPlan",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("day", models.CharField(choices=[("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Thursday","Thursday"),("Friday","Friday"),("Saturday","Saturday"),("Sunday","Sunday")], max_length=12)),
                ("meal_type", models.CharField(choices=[("Breakfast","Breakfast"),("Lunch","Lunch"),("Dinner","Dinner")], max_length=12)),
                ("recipe", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="planner.recipe")),
            ],
            options={"unique_together": {("day","meal_type")}},
        ),
    ]
