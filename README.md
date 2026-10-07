# Recipe & Meal Planner

**Project by:** Vidushi Mishra

## 1. Project Overview

Recipe & Meal Planner is a Django-based web application designed to help users organize recipes and plan meals for the week. The application provides a simple way to store recipes, view their details, update or remove them, and assign recipes to different days and meal types.

The project addresses the common problem of deciding and organizing meals repeatedly by bringing recipe management and meal planning into one web application.

## 2. Problem Statement

Planning meals manually can become repetitive and time-consuming. Users may have recipes saved in different places but still struggle to decide what to prepare on a particular day.

The problem is to develop a simple system where users can:

- Store and manage recipes in one place.
- View ingredients and cooking instructions easily.
- Organize meals according to days of the week.
- Assign recipes to breakfast, lunch, or dinner.
- Modify or remove recipes and meal plans when required.

## 3. Proposed Solution

The proposed solution is a web-based Recipe & Meal Planner developed using Django and SQLite.

The application maintains recipe information in a database and provides an interface through which users can manage recipes. A separate meal-planning section allows recipes to be assigned to specific days and meal types.

This reduces manual planning and provides a centralized system for recipe storage and weekly meal organization.

## 4. Objectives

1. To develop a user-friendly recipe management system.
2. To store recipe information in a structured database.
3. To allow users to add, view, edit, and delete recipes.
4. To provide a weekly meal-planning facility.
5. To demonstrate the use of Django models, views, forms, templates, and database operations.
6. To create a practical web application using Python and Django.

## 5. Key Features

### Recipe Management
- Add a new recipe.
- View all saved recipes.
- View complete recipe details.
- Edit existing recipes.
- Delete recipes.
- Store category, ingredients, instructions, and cooking time.

### Meal Planning
- Add a recipe to the meal plan.
- Select a day of the week.
- Select breakfast, lunch, or dinner.
- View planned meals.
- Remove meals from the plan.

### Dashboard
The home page provides a simple overview of:
- Number of saved recipes.
- Number of planned meals.
- Number of days supported by the planner.

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Web application framework |
| SQLite | Database |
| HTML | Web page structure |
| CSS | User interface styling |

## 7. Project Structure

```text
recipe-meal-planner/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── recipe_planner/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── planner/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│
└── templates/
    ├── base.html
    ├── home.html
    ├── recipe_list.html
    ├── recipe_detail.html
    ├── recipe_form.html
    ├── recipe_confirm_delete.html
    ├── meal_plan.html
    ├── meal_plan_form.html
    └── meal_plan_confirm_delete.html
```

## 8. How the Application Works

### Step 1: Recipe Creation
The user opens the **Add Recipe** page and enters:
- Recipe name
- Category
- Ingredients
- Instructions
- Cooking time

The information is submitted through a Django form and stored in the SQLite database.

### Step 2: Recipe Viewing
The Recipes page retrieves stored recipes from the database and displays them. Selecting a recipe opens its complete details.

### Step 3: Recipe Modification
Users can edit an existing recipe when information needs to be changed.

### Step 4: Recipe Deletion
A recipe can be removed through the delete option after confirmation.

### Step 5: Meal Planning
The user selects:
- A day
- A meal type
- A recipe

The selected recipe is then added to the weekly meal plan.

### Step 6: Meal Plan Management
The Meal Plan page displays the planned meals and allows users to remove entries when required.

## 9. Database Design

The application uses two main models:

### Recipe

| Field | Description |
|---|---|
| name | Name of the recipe |
| category | Breakfast, Lunch, Dinner, Snack, or Dessert |
| ingredients | Ingredients required |
| instructions | Preparation instructions |
| cooking_time | Cooking time in minutes |

### MealPlan

| Field | Description |
|---|---|
| day | Day of the week |
| meal_type | Breakfast, Lunch, or Dinner |
| recipe | Recipe selected for the meal |

The `MealPlan` model uses a relationship with the `Recipe` model so that a planned meal is connected to a stored recipe.

## 10. Installation and Setup

### Prerequisites

- Python 3.x
- pip
- A web browser

### Install Dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Start the Development Server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 11. Expected Output

The application provides:

- A home/dashboard page.
- A recipe listing page.
- Recipe detail pages.
- Forms for adding and editing recipes.
- Delete functionality.
- A weekly meal-planning page.
- Forms for adding meals to the plan.
- A simple responsive-style interface using HTML and CSS.

## 12. Advantages

- Simple and easy-to-use interface.
- Centralized recipe storage.
- Reduces repetitive meal-planning work.
- Easy recipe modification and deletion.
- Uses a lightweight SQLite database.
- Django provides a structured and scalable application architecture.

## 13. Future Scope

The application can be extended with:

- User registration and login.
- Personalized meal plans for different users.
- Recipe search and filtering.
- Nutritional information and calorie tracking.
- Automatic meal-plan generation.
- Grocery-list generation from planned recipes.
- Recipe images.
- Mobile-friendly improvements.
- Cloud database support.
- Recommendation features based on user preferences.

## 14. Conclusion

The Recipe & Meal Planner demonstrates how a practical meal-management problem can be converted into a web-based software solution.

Using Django, the project combines recipe management with weekly meal planning in a single application. It demonstrates important web-development concepts including database models, forms, views, URL routing, templates, CRUD operations, and database relationships.

The project can serve as a foundation for a more advanced personalized meal-planning application.

## 15. Reference

The project concept and general problem/solution direction were referred to from the following GeeksforGeeks resource:

**Recipe Meal Planner using Django**  
https://www.geeksforgeeks.org/python/recipe-meal-planner-using-django/

The implementation in this repository is organized as an educational project for demonstrating Django-based recipe and meal-planning functionality.
