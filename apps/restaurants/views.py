from typing import Optional
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.managers.models import RestaurantManager

from apps.restaurants.models import Restaurant
from apps.managers.permissions import IsManager
from apps.restaurants.serializers import RestaurantSerializer


class RestaurantView(APIView):
    queryset = Restaurant.objects.none()
    permission_classes = [IsManager]
    serializer_class = RestaurantSerializer

    @staticmethod
    def get_restaurant(user) -> Optional[Restaurant]:
        # TODO: better to move it to User model class
        try:
            manager = user.restaurantmanager
        except RestaurantManager.DoesNotExist:
            return None
        return manager.restaurant

    def get(self, request) -> Response:
        restaurant = self.get_restaurant(request.user)

        if not restaurant:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(restaurant)
        return Response(serializer.data)

    def put(self, request) -> Response:
        restaurant = self.get_restaurant(request.user)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
