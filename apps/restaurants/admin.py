from django.contrib import admin

from apps.restaurants.models import Restaurant, RestaurantManager


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    fields = ["tenant", "name", "description"]


@admin.register(RestaurantManager)
class RestaurantManagerAdmin(admin.ModelAdmin):
    fields = ["tenant", "user", "restaurant"]
