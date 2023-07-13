from django.db import models
from django.contrib.auth.models import User

from apps.tenants.models import TenantAwareModel


class Restaurant(TenantAwareModel):
    tenant = models.OneToOneField("tenants.Tenant", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()


class RestaurantManager(TenantAwareModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "restaurant")
