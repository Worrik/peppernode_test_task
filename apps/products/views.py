from rest_framework import viewsets, pagination

from apps.restaurants.permissions import IsManagerOrReadOnly
from apps.tenants.utils import tenant_from_request

from .models import Category
from .models import Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsManagerOrReadOnly]

    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsManagerOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("category")

        tenant = tenant_from_request(self.request)
        qs = qs.filter(tenant=tenant)

        category = self.request.GET.get("category")
        if category:
            qs = qs.filter(category=category)

        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(name__icontains=q)

        # filter possible order by values
        order_by = [
            field
            for field in self.request.GET.getlist("order_by")
            if field.lstrip("-") in ("name", "price", "category")
            and field.count("-") <= 1
        ]
        if order_by:
            qs = qs.order_by(*order_by)

        return qs
