from django.contrib import admin

from apps.products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]

    # If managers need to access admin
    # def get_queryset(self, request: HttpRequest) -> QuerySet:
    #     tenant = tenant_from_request(request)
    #     return super().get_queryset(request).filter(tenant=tenant)

    # def save_model(
    #     self, request: HttpRequest, obj: Category, form: Any, change: Any
    # ) -> None:
    #     tenant = tenant_from_request(request)
    #     obj.tenant = tenant
    #     return super().save_model(request, obj, form, change)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ["category", "name", "price"]
