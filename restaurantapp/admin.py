from django.contrib import admin
from .models import Ingrediants, MenuItems, RecipeRequirements, PurchaseLog

# Register your models here.


class IngregdiantsAdmin(admin.ModelAdmin):
    list_display = ["name", "available_quantity", "price_per_unit", "unit"]
    list_filter = ["name", "available_quantity"]

    def __str__(self):
        return self.id

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_filter = ["name", "price"]

    def __str__(self):
        return self.id


class RecipeRequirementsAdmin(admin.ModelAdmin):
    list_display = ["menu", "ingrediant"]
    


admin.site.register(Ingrediants)
admin.site.register(MenuItems)
admin.site.register(RecipeRequirements)
admin.site.register(PurchaseLog)