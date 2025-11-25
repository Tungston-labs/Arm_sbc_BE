from rest_framework import serializers
from .models import Product, Processor, Board


# -------------------------
# EXISTING PRODUCT SERIALIZER
# -------------------------
class ProductSerializer(serializers.ModelSerializer):
    available = serializers.BooleanField(default=True)
    image = serializers.ImageField(use_url=True)  # ensures URL usage

    class Meta:
        model = Product
        fields = '__all__'


# -------------------------
# NEW: MINI BOARD SERIALIZER (for catalog)
# -------------------------
class BoardMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = [
            "id",
            "name",
            "slug",
            "short_tagline",
            "dram_config",
            "emmc_config",
            "wifi",
            "ethernet",
            "video_connectors",
            "expansion",
        ]


# -------------------------
# NEW: PROCESSOR SERIALIZER (includes boards)
# -------------------------
class ProcessorCatalogSerializer(serializers.ModelSerializer):
    boards = BoardMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Processor
        fields = [
            "id",
            "vendor",
            "code",
            "name",
            "cpu_cores",
            "cpu_arch",
            "npu_tops",
            "max_dram_gb",
            "hdmi",
            "lvds",
            "edp",
            "dp",
            "mipi_dsi",
            "usb2_ports",
            "usb3_ports",
            "pcie_desc",
            "ethernet_cap",
            "sata",
            "sdio",
            "boards",
        ]


# -------------------------
# NEW: VENDOR SERIALIZER (top-level grouping)
# -------------------------
class VendorCatalogSerializer(serializers.Serializer):
    vendor = serializers.CharField()
    processors = ProcessorCatalogSerializer(many=True)
