import uuid
from django.db import models
from shared.models import TimeStampedModel
from product.models import Product
from cart.models import Cart

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('open', 'Open'),
    ('closed', 'Closed'),
]

class ProductInquiry(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Product, related_name="inquiries")
    
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    delivery_location = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Inquiry {self.id} - {self.email}"
