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
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="processors"
    )

    # IDENTIFICATION
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

    # --- REQUIRED SoC FIELDS ---
    soc = models.CharField(max_length=100, blank=True, null=True)                 
    architecture = models.CharField(max_length=100, blank=True, null=True)        
    cpu = models.CharField(max_length=200, blank=True, null=True)                 
    max_clock = models.CharField(max_length=100, blank=True, null=True)           
    gpu = models.CharField(max_length=100, blank=True, null=True)
    npu = models.CharField(max_length=100, blank=True, null=True)                 
    l1_cache = models.CharField(max_length=100, blank=True, null=True)
    l2_l3_cache = models.CharField(max_length=100, blank=True, null=True)
    max_ram = models.CharField(max_length=100, blank=True, null=True)             

    # =============================
    #  DISPLAY CAPABILITY (ENUMS)
    # =============================
    HDMI_CHOICES = [
        ("none", "Not Supported"),
        ("1.4", "HDMI 1.4"),
        ("2.0", "HDMI 2.0"),
        ("2.1", "HDMI 2.1"),
    ]

    LVDS_CHOICES = [
        ("none", "Not Supported"),
        ("single", "Single-channel LVDS"),
        ("dual", "Dual-channel LVDS"),
    ]

    EDP_CHOICES = [
        ("none", "Not Supported"),
        ("1.1", "eDP 1.1"),
        ("1.2", "eDP 1.2"),
        ("1.3", "eDP 1.3"),
        ("1.4", "eDP 1.4"),
    ]

    DP_CHOICES = [
        ("none", "Not Supported"),
        ("1.2", "DisplayPort 1.2"),
        ("1.4", "DisplayPort 1.4"),
        ("2.0", "DisplayPort 2.0"),
    ]

    DSI_CHOICES = [
        ("none", "Not Supported"),
        ("2-lane", "MIPI DSI 2-lane"),
        ("4-lane", "MIPI DSI 4-lane"),
    ]

    hdmi = models.CharField(max_length=10, choices=HDMI_CHOICES, default="none")
    lvds = models.CharField(max_length=10, choices=LVDS_CHOICES, default="none")
    edp = models.CharField(max_length=10, choices=EDP_CHOICES, default="none")
    dp = models.CharField(max_length=10, choices=DP_CHOICES, default="none")
    dsi = models.CharField(max_length=10, choices=DSI_CHOICES, default="none")



    USB2_CHOICES = [
        ("none", "Not Supported"),
        ("1-port", "1 Port"),
        ("2-port", "2 Ports"),
        ("4-port", "4 Ports"),
    ]

    USB3_CHOICES = [
        ("none", "Not Supported"),
        ("1-port", "1 Port"),
        ("2-port", "2 Ports"),
    ]

    usb2 = models.CharField(max_length=10, choices=USB2_CHOICES, default="none")
    usb3 = models.CharField(max_length=10, choices=USB3_CHOICES, default="none")

    sdio = models.BooleanField(default=False)
    sata = models.BooleanField(default=False)

    ETHERNET_CHOICES = [
        ("none", "Not Supported"),
        ("10/100", "10/100 Mbps MAC"),
        ("1g", "1G Ethernet MAC"),
        ("2.5g", "2.5G Ethernet MAC"),
    ]

    ethernet_mac = models.CharField(
        max_length=20, choices=ETHERNET_CHOICES, default="none"
    )

    # IMAGE
    image = models.ImageField(upload_to="processors/", blank=True, null=True)

    class Meta:
        ordering = ["vendor", "code"]

    def __str__(self):
        return f"{self.vendor.name} {self.code}"



class Product(TimeStampedModel):
    # Core relations
    processor = models.ForeignKey(
        Processor,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )

    class EthernetType(models.TextChoices):
        NONE = "NONE", "No Ethernet"
        ETH_10_100 = "10_100", "10/100 Mbps"
        ETH_1G = "1G", "1 Gigabit"
        ETH_DUAL_1G = "DUAL_1G", "Dual Gigabit"

    ethernet = models.CharField(
        max_length=20,
        choices=EthernetType.choices,
        default=EthernetType.NONE
    )

    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=150)
    short_tagline = models.CharField(max_length=255, blank=True)

    dram_config = models.CharField(max_length=150, blank=True)    # MEMORY
    emmc_config = models.CharField(max_length=150, blank=True)    # eMMC
    storage_slots = models.CharField(max_length=200, blank=True)

    wifi = models.CharField(max_length=150, blank=True)
    video_connectors = models.CharField(max_length=200, blank=True)
    expansion = models.CharField(max_length=200, blank=True)
    gpio_headers = models.CharField(max_length=200, blank=True)

    power_input = models.CharField(max_length=150, blank=True)
    form_factor = models.CharField(max_length=150, blank=True)

    additional_info = models.JSONField(blank=True, null=True)

    ram_gb = models.PositiveIntegerField()
    storage = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)



    memory_type = models.CharField(max_length=100, blank=True)      

                

    hdmi_in = models.BooleanField(default=False)                    
    hdmi_out = models.BooleanField(default=False)               

    dp = models.BooleanField(default=False)                        
    lvds = models.BooleanField(default=False)                   
    edp = models.BooleanField(default=False)                      
    dsi = models.BooleanField(default=False)                     

    usb2 = models.BooleanField(default=False)                       
    usb3 = models.BooleanField(default=False)                       
    type_c = models.BooleanField(default=False)                    

    debug_port = models.BooleanField(default=False)                 
    speaker = models.BooleanField(default=False)                  
    audio_amplifier = models.BooleanField(default=False)           

    rs232 = models.BooleanField(default=False)                    
    rs485 = models.BooleanField(default=False)                     

    front_image = models.ImageField(upload_to="products/front/", blank=True, null=True)
    back_image = models.ImageField(upload_to="products/back/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
