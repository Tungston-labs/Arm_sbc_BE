import uuid
from django.db import models
from shared.models import TimeStampedModel


class Product(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ram = models.CharField(max_length=50, blank=True, null=True)
    cores = models.PositiveIntegerField(blank=True, null=True)
    storage = models.CharField(max_length=100, blank=True, null=True)
    specs = models.JSONField(blank=True, null=True, default=dict)
    """
    Example:
    {
        "processor": {"cpu": "Intel i7", "socket": "LGA1200", "bios": "v2.0", "secure_flash": True},
        "memory": {"technology": "DDR4", "capacity": "16GB", "socket": "DIMM1"},
        "expansion_slots": {"M.2": 2, "HDMI": 1, "DisplayPort": 2, ...},
        "ethernet": {"controller": "Intel I219", "speed": "1Gbps", "connector": "RJ45"},
        "graphics": {"controller": "NVIDIA GTX 1650", "HDMI":1, "DP":1, "eDP":0, "multi_display": True},
        "storage": {"M.2": "512GB", "SATA": "1TB"},
        "power": {"input": "100-240V", "internal_connector": ["USB","COM","GPIO"]},
        "audio": {"interface": "HD Audio"},
        "security": {"TPM": True},
        "watchdog": {"output": "GPIO", "interval": "1min"},
        "environment": {"operating_temp": "0-70C","storage_temp":"-20-85C","operating_humidity":"10-90%","storage_humidity":"5-95%"}
    }
    """

    additional_info = models.JSONField(blank=True, null=True, default=dict)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#from django.db import models


class Vendor(models.TextChoices):
    ROCKCHIP = "rockchip", "Rockchip"
    ALLWINNER = "allwinner", "Allwinner"


class Processor(models.Model):

    class Vendor(models.TextChoices):
        ROCKCHIP = "rockchip", "Rockchip"
        ALLWINNER = "allwinner", "Allwinner"

    vendor = models.CharField(
        max_length=20,
        choices=Vendor.choices,
        db_index=True,
    )

    code = models.CharField(max_length=50, unique=True)   # e.g. "RK3588"
    name = models.CharField(max_length=100)               # e.g. "Rockchip RK3588"

    # ---- CPU BASE INFO ----
    cpu_cores = models.PositiveIntegerField(null=True, blank=True)
    cpu_arch = models.CharField(max_length=100, blank=True)   # e.g. "4xA76 + 4xA55"
    arch_bits = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="32 or 64 bit CPU architecture"
    )

    # ---- CACHE INFORMATION ----
    l1_cache_kb = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Total L1 cache in KB"
    )
    l2_cache_kb = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Total L2 cache in KB"
    )

    # ---- GPU ----
    gpu = models.CharField(
        max_length=100,
        blank=True,
        help_text="GPU model e.g. Mali-G610 MP4"
    )

    # ---- AI / MEMORY ----
    npu_tops = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="NPU TOPS rating (e.g. 6.00)"
    )
    max_dram_gb = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Maximum supported DRAM (GB)"
    )

    # ---- DISPLAY INTERFACES ----
    hdmi = models.BooleanField(default=False)
    lvds = models.BooleanField(default=False)
    edp = models.BooleanField(default=False)
    dp = models.BooleanField(default=False)
    mipi_dsi = models.BooleanField(default=False)

    # ---- I/O CAPABILITIES ----
    usb2_ports = models.PositiveIntegerField(null=True, blank=True)
    usb3_ports = models.PositiveIntegerField(null=True, blank=True)
    pcie_desc = models.CharField(max_length=100, blank=True)      # e.g. "1×4 + 2×1 Gen3"
    ethernet_cap = models.CharField(max_length=100, blank=True)   # e.g. "1G / 2.5G MAC"
    sata = models.BooleanField(default=False)
    sdio = models.BooleanField(default=True)

    # ---- EXTRA (future-proof) ----
    extra = models.JSONField(blank=True, null=True)

    # ---- CHIP PHOTO ----
    image = models.ImageField(
        upload_to="processors/",
        blank=True,
        null=True,
        help_text="Upload chip photo (.png or .jpg)"
    )

    class Meta:
        ordering = ["vendor", "code"]

    def __str__(self):
        return f"{self.get_vendor_display()} {self.code}"

class Board(models.Model):
    processor = models.ForeignKey(
        Processor, on_delete=models.CASCADE, related_name="boards"
    )

    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=150)  # e.g. "ARM-SBC-EDGE-3588"
    short_tagline = models.CharField(max_length=255, blank=True)

    # Board-level specs
    dram_config = models.CharField(max_length=150, blank=True)  # "8/16GB LPDDR4X"
    emmc_config = models.CharField(max_length=150, blank=True)  # "32/64/128GB eMMC"
    storage_slots = models.CharField(
        max_length=200, blank=True
    )  # "M.2 NVMe, microSD"

    wifi = models.CharField(max_length=150, blank=True)  # "AP6275P WiFi 6 + BT5.0"
    ethernet = models.CharField(
        max_length=200, blank=True
    )  # "1x 1G, 1x 2.5G, PoE"
    video_connectors = models.CharField(
        max_length=200, blank=True
    )  # "HDMI 2.1, eDP, LVDS"
    expansion = models.CharField(
        max_length=200, blank=True
    )  # "2x M.2, 1x mini-PCIe"
    gpio_headers = models.CharField(
        max_length=200, blank=True
    )  # "40-pin GPIO, FPC for LVDS"

    power_input = models.CharField(max_length=150, blank=True)  # "12V DC, 5.5x2.1mm"
    form_factor = models.CharField(max_length=150, blank=True)  # "100 x 100 mm"

    # Optional link to existing Product if you want
    # from .models import Product   # if your Product is here
    # product = models.OneToOneField(
    #     Product, on_delete=models.SET_NULL,
    #     null=True, blank=True, related_name="board"
    # )

    additional_info = models.JSONField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    image = models.ImageField(
        upload_to="processors/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
