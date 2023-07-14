from django.contrib.auth.models import User
from django.db import models


class RestaurantManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.OneToOneField(
        "restaurants.Restaurant", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("user", "restaurant")
