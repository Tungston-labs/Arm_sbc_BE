# apps/cart/models.py
import uuid
from django.db import models
from shared.models import TimeStampedModel
from product.models import Product
from django.conf import settings

class Cart(TimeStampedModel):
    """
    Cart can be associated with a user (admin or future customer model) or with a guest token.
    Frontend should store 'cart_token' (UUID string) in cookie/localStorage for guest users.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    cart_token = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f"Cart {self.id} - user:{self.user} token:{self.cart_token}"

class CartItem(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_add = models.DecimalField(max_digits=12, decimal_places=2, default=0)  

    class Meta:
        unique_together = ('cart', 'product')
