from rest_framework import serializers
from .models import Processor, Board, Vendor


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


class VendorCatalogSerializer(serializers.Serializer):
    vendor = serializers.CharField()
    processors = ProcessorCatalogSerializer(many=True)
