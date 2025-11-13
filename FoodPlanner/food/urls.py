from django.urls import path
from .views import *
urlpatterns = [
    path("", index,name='home'),
    path("show/edit/", edit_ing),
    path("show/", show_ingredients,name='show'),
    path("add/",edit_recipe),
    path("suggested/",suggest),
    path("week/",weekly_plan),


]
