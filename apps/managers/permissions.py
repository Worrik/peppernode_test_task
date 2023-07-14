from rest_framework import permissions
from rest_framework.permissions import BasePermission
from .models import RestaurantManager
import logging


class IsManager(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        try:
            has_manager = (
                user.is_authenticated and user.restaurantmanager is not None
            )
        except RestaurantManager.DoesNotExist:
            has_manager = False

        return has_manager


class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user

        try:
            has_manager = (
                user.is_authenticated and user.restaurantmanager is not None
            )
        except RestaurantManager.DoesNotExist:
            has_manager = False

        return has_manager
