from rest_framework import serializers

from apps.tenants.utils import tenant_from_request
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context["request"]
        tenant = tenant_from_request(request)
        validated_data["tenant"] = tenant
        return super().create(validated_data)

    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    def create(self, validated_data):
        request = self.context["request"]
        tenant = tenant_from_request(request)
        validated_data["tenant"] = tenant
        return super().create(validated_data)

    class Meta:
        model = Product
        fields = ["id", "category", "name", "price"]
