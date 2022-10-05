from msilib.schema import ListView
from django.shortcuts import render
from .models import Ingrediants, MenuItems, RecipeRequirements, PurchaseLog
from django.views.generic import ListView

# Create your views here.


class GetIngrediants(ListView):

    def get(self, request):
        all_ingrediants = Ingrediants.objects.all().order_by("-id")
        ing_count = Ingrediants.objects.all().count()
        context = {
            "all_ingrediants": all_ingrediants,
            "ing_count": ing_count
        }
        print(context)
        return render(request, "restaurantapp/index.html", context)
