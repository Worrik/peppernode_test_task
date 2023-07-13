from django.contrib import admin

from apps.tenants.models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    fields = ["name", "subdomain_prefix"]
