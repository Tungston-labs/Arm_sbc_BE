from django.contrib import admin
from .models import Product, Processor, Board


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "ram", "storage", "available")
    search_fields = ("name",)


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ("code", "vendor", "cpu_cores", "npu_tops", "max_dram_gb")
    list_filter = ("vendor",)
    search_fields = ("code", "name")


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("name", "processor", "dram_config", "emmc_config")
    list_filter = ("processor",)
    search_fields = ("name", "slug")
