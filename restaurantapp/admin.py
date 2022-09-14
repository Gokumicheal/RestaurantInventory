from django.contrib import admin
from .models import Ingrediants, MenuItems, RecipeRequirements, PurchaseLog

# Register your models here.

admin.site.register(Ingrediants)
admin.site.register(MenuItems)
admin.site.register(RecipeRequirements)
admin.site.register(PurchaseLog)