from django.contrib import admin
from .models import Category, Vendor, Processor,  Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    fields = ("name", "ram_gb", "price", "available")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "created_at")
    search_fields = ("name",)
    list_filter = ("category",)


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ("id", "vendor", "code", "name", "cpu_cores", "updated_at")
    search_fields = ("code", "name")
    list_filter = ("vendor", "arch_bits", "hdmi", "dp", "mipi_dsi")
    inlines = [ProductInline]
    readonly_fields = ("created_at", "updated_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "processor", "ram_gb", "price", "available")
    search_fields = ("name",)
    list_filter = ("processor", "available")
    readonly_fields = ("created_at", "updated_at")
