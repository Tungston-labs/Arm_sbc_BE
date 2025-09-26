import uuid
from django.db import models
from shared.models import TimeStampedModel
from product.models import Product

class Review(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)  
    email = models.EmailField()               
    rating = models.PositiveSmallIntegerField()  
    review = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=True)  

    def __str__(self):
        return f"Review {self.id} - {self.product.name} - {self.rating}"
