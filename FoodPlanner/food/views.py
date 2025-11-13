
from django.dispatch import receiver
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Ingredients,FoodRecipes
from  .forms import IngForm,RecipeForm
# Create your views here.

def index(request):
    
    return render(request, 'food/index.html')






def show_ingredients(request):
    ingredients= Ingredients.objects.all()
    context={
        'ingredients':ingredients
    }
    return render(request, 'food/show.html',context)





def edit_ing(request):
    if request.method == 'POST':
        form=IngForm(request.POST)
        if form.is_valid():
            new_item_name=form.cleaned_data['name'].lower()
            all_ingredients=Ingredients.objects.all()
            for item  in all_ingredients:
                if item.name.lower() == new_item_name:
                    item.quantity=form.cleaned_data['quantity']
                    item.save()
                    return redirect(reverse('show'))
            # save data and return user to the home page
            form.save()   
            return redirect(reverse('show'))
    

    else:
        form = IngForm()
    context={
        'form':form
    }
    return render(request, 'food/edit-ing.html',context)









def edit_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect(reverse('home'))
    else:
        form = RecipeForm()
    context={
        'form':form
    }
    return render(request, 'food/edit-recipe.html',context)






def suggest(request):
    suggested_food=[]
    recipes= FoodRecipes.objects.all()
    ingredients=Ingredients.objects.all()
    for food in recipes:
        existing_ingrdients=0
        required_ingredients=food.recipe.all()
        for req_ing in required_ingredients:
            for ex_ing in ingredients:
                if ex_ing==req_ing:
                    if ex_ing.quantity>0:
                        existing_ingrdients+=1
        if existing_ingrdients== food.needed_ings_amount:
            suggested_food.append(food.name)  
     

    context={
        'suggested_food':suggested_food
       
    }
    return render(request, 'food/suggest.html',context)








def weekly_plan(request):
    recipes=FoodRecipes.objects.all()
   

    buy_list=[]
    week_list=[]
    while len(week_list)<=14:
        for food in recipes:
            buy=food.recipe.all()
            for item in buy:
                buy_list.append(item.name)

            week_list.append(food.name)
   


    buy_list=set(buy_list)
    while len(week_list)>14:
        week_list.pop()
   
    context={
        'week_list':week_list,
        'buy_list':buy_list
    }

    return render(request,'food/week.html',context)
            