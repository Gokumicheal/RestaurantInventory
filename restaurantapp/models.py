from django.db import models

# Create your models here.

unit_choices = [
    ("kg", "KG"),
    ("gm", "Gram"),
    ("lr", "Litre"),
    ("ou", "Ounces"),
    ("eg", "Eggs"),
    ("lb", "lbs")
]

class Ingrediants(models.Model):
    name = models.CharField(max_length=200)
    available_quantity = models.FloatField()
    price_per_unit = models.FloatField()
    unit = models.CharField(max_length=2, choices=unit_choices)


class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()



class RecipeRequirements(models.Model):
    menu = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingrediant = models.ForeignKey(Ingrediants, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)


class PurchaseLog(models.Model):
    menu = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    quantity = models.FloatField(default=1)

