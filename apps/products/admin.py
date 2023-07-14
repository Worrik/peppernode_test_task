from django.contrib import admin

from apps.products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ["category", "name", "price"]
