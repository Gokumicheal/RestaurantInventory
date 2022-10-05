from django.urls import path
from .views import GetIngrediants

urlpatterns = [
    path("", GetIngrediants.as_view(), name="GetIngrediants"),
]
