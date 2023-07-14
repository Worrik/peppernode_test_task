from django.contrib import admin

from apps.managers.models import RestaurantManager


@admin.register(RestaurantManager)
class RestaurantManagerAdmin(admin.ModelAdmin):
    fields = ["user", "restaurant"]
