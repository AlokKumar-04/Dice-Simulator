from django.urls import path
from . import views


app_name = 'Dice'

urlpatterns = [
    path("", views.RollDice, name="RollDice"),
    path("clear history/", views.clear_dice_history, name='clear_dice_history'),
]
