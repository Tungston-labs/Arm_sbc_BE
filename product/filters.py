import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    ram_gb = django_filters.NumberFilter(field_name="ram_gb")
    memory_type = django_filters.CharFilter(field_name="memory_type", lookup_expr="iexact")
    storage = django_filters.CharFilter(field_name="storage", lookup_expr="icontains")
    available = django_filters.BooleanFilter(field_name="available")

    ethernet = django_filters.CharFilter(method="filter_ethernet")

    def filter_ethernet(self, queryset, name, value):
        value = value.lower().strip()
        if value == "gigabit":
            return queryset.filter(ethernet__in=["1G", "DUAL_1G"])
        elif value == "fast":
            return queryset.filter(ethernet="10_100")
        elif value == "none":
            return queryset.filter(ethernet="NONE")
        return queryset


    class Meta:
        model = Product
        fields = ["ram_gb", "memory_type", "storage", "available"]
