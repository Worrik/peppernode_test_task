from django.db import models
from django_tenants.models import TenantMixin
from django_tenants.models import DomainMixin


class Domain(DomainMixin):
    pass


class Restaurant(TenantMixin):
    name = models.CharField(max_length=255)
    description = models.TextField()

    auto_create_schema = True
