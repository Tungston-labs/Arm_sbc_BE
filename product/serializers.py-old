from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    available = serializers.BooleanField(default=True)
    image = serializers.ImageField(use_url=True)  # ensures URL usage

    class Meta:
        model = Product
        fields = '__all__'
