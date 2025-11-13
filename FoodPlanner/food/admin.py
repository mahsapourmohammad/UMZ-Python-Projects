from django.contrib import admin
from .models import FoodRecipes,Ingredients
# Register your models here.

admin.site.register(Ingredients)
admin.site.register(FoodRecipes)