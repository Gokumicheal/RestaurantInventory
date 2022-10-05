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

    class Meta:
        verbose_name_plural = "Ingrediants"

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    class Meta:
        verbose_name_plural = "Menu Items"
   
    def __str__(self):
        return self.name



class RecipeRequirements(models.Model):
    menu = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingrediant = models.ForeignKey(Ingrediants, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "Recipe Requirements"


class PurchaseLog(models.Model):
    menu = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu.name

