from django.contrib import admin
from .models import Category, Vendor, Processor, Board, Product


class BoardInline(admin.TabularInline):
    model = Board
    extra = 1
    fields = ("name", "slug", "is_active")


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
    inlines = [BoardInline, ProductInline]
    readonly_fields = ("created_at", "updated_at")


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "processor", "is_active", "updated_at")
    search_fields = ("name", "slug")
    list_filter = ("is_active", "processor__vendor")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "processor", "board", "ram_gb", "price", "available")
    search_fields = ("name",)
    list_filter = ("processor", "available")
    readonly_fields = ("created_at", "updated_at")
