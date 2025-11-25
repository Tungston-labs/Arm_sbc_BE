from rest_framework import serializers
from .models import ProductInquiry
from product.models import Product
from cart.models import Cart

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'image', 'description', 'ram', 'cores', 'storage',
            'specs', 'additional_info', 'available'
        ]

from rest_framework import serializers
from .models import ProductInquiry
from product.models import Product
from cart.models import Cart

class ProductInquirySerializer(serializers.ModelSerializer):
    product_ids = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True,
        required=True
    )
    cart_id = serializers.UUIDField(write_only=True, required=False, allow_null=True)
    products = ProductDetailSerializer(many=True, read_only=True)

    class Meta:
        model = ProductInquiry
        fields = [
            'id', 'cart_id', 'products', 'product_ids', 'first_name', 'last_name',
            'company_name', 'email', 'phone', 'address', 'country', 'state',
            'delivery_location', 'description', 'status'
        ]
        read_only_fields = ['id', 'products']

    def create(self, validated_data):
        product_ids = validated_data.pop('product_ids', [])
        cart_id = validated_data.pop('cart_id', None)
        cart = Cart.objects.filter(id=cart_id).first() if cart_id else None

        inquiry = ProductInquiry.objects.create(cart=cart, **validated_data)

        # Add products to Many-to-Many relation
        products = Product.objects.filter(id__in=product_ids)
        inquiry.products.set(products)

        return inquiry
