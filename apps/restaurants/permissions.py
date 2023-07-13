from rest_framework import permissions
from rest_framework.permissions import BasePermission
from apps.restaurants.models import RestaurantManager

from apps.tenants.utils import tenant_from_request


class IsManager(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        try:
            has_manager = (
                user.is_authenticated and user.restaurantmanager is not None
            )
        except RestaurantManager.DoesNotExist:
            has_manager = False

        tenant = tenant_from_request(request)
        return has_manager and user.restaurantmanager.tenant == tenant


class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        tenant = tenant_from_request(request)

        try:
            has_manager = (
                user.is_authenticated and user.restaurantmanager is not None
            )
        except RestaurantManager.DoesNotExist:
            has_manager = False

        return has_manager and user.restaurantmanager.tenant == tenant
