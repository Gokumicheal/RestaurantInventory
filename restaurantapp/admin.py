from django.contrib import admin
from .models import Ingrediants, MenuItems, RecipeRequirements, PurchaseLog

# Register your models here.


class IngregdiantsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "available_quantity", "price_per_unit", "unit"]
    list_filter = ["id", "name", "available_quantity"]


class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price"]
    list_filter = ["id", "name", "price"]


class RecipeRequirementsAdmin(admin.ModelAdmin):
    list_display = ["id", "menu", "ingrediant", "quantity"]

class PurchaseLogAdmin(admin.ModelAdmin):
    list_display = ["id", "menu", "timestamp"]
    

admin.site.register(Ingrediants, IngregdiantsAdmin)
admin.site.register(MenuItems, MenuItemsAdmin)
admin.site.register(RecipeRequirements, RecipeRequirementsAdmin)
admin.site.register(PurchaseLog, PurchaseLogAdmin)