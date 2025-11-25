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
