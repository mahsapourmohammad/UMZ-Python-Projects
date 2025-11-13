from django import forms
from .models import Ingredients,FoodRecipes



class IngForm(forms.ModelForm):
    
    class Meta:
        model = Ingredients
        fields = ['name', 'quantity', 'quantity_value']







class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = FoodRecipes
        fields = '__all__'
