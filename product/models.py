from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Vendor(TimeStampedModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="vendors"
    )
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="vendors/", blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    
    website_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.category.name})"




class Processor(TimeStampedModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="processors")

    code = models.CharField(max_length=50, unique=True)          # e.g. "RK3588"
    name = models.CharField(max_length=100)                      # e.g. "Rockchip RK3588"

    # CPU BASE INFO
    cpu_cores = models.PositiveIntegerField(null=True, blank=True)
    cpu_arch = models.CharField(max_length=100, blank=True)      # "4xA76 + 4xA55"
    arch_bits = models.CharField(null=True, blank=True)
    ram_expandable_upto= models.PositiveIntegerField(null=True, blank=True)

    # CACHE
    l1_cache_kb = models.CharField(null=True, blank=True)
    l2_cache_kb = models.CharField(null=True, blank=True)

    # GPU
    gpu = models.CharField(max_length=100, blank=True)

    # AI / MEMORY
    npu_tops = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    max_dram_gb = models.CharField(null=True, blank=True)

    # DISPLAY
    hdmi = models.BooleanField(default=False)
    lvds = models.BooleanField(default=False)
    edp = models.BooleanField(default=False)
    dp = models.BooleanField(default=False)
    mipi_dsi = models.BooleanField(default=False)

    # I/O
    usb2_ports = models.CharField(null=True, blank=True)
    usb3_ports = models.CharField(null=True, blank=True)
    pcie_desc = models.CharField(max_length=100, blank=True)
    ethernet_cap = models.CharField(max_length=100, blank=True)
    sata = models.BooleanField(default=False)
    sdio = models.BooleanField(default=True)

    # Extra Info
    extra = models.JSONField(blank=True, null=True)
    """JSON expected: """
    # Image
    image = models.ImageField(upload_to="processors/", blank=True, null=True)

    class Meta:
        ordering = ["vendor", "code"]

    def __str__(self):
        return f"{self.vendor.name} {self.code}"


# --------------------------------------------------------
# BOARD  (Your exact model)
# --------------------------------------------------------
class Product(TimeStampedModel):
    # Core relations
    processor = models.ForeignKey(
        Processor, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="products"
    )

    # Basic product info
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=150)
    short_tagline = models.CharField(max_length=255, blank=True)

    # Board-level hardware specs
    dram_config = models.CharField(max_length=150, blank=True)
    emmc_config = models.CharField(max_length=150, blank=True)
    storage_slots = models.CharField(max_length=200, blank=True)

    wifi = models.CharField(max_length=150, blank=True)
    ethernet = models.CharField(max_length=200, blank=True)
    video_connectors = models.CharField(max_length=200, blank=True)
    expansion = models.CharField(max_length=200, blank=True)
    gpio_headers = models.CharField(max_length=200, blank=True)

    power_input = models.CharField(max_length=150, blank=True)
    form_factor = models.CharField(max_length=150, blank=True)

    additional_info = models.JSONField(blank=True, null=True)

    # Commercial product-specific fields
    ram_gb = models.PositiveIntegerField()
    storage = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    # Product image
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
