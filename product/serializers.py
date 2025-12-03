from rest_framework import serializers
from .models import Category, Vendor, Processor, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    class Meta:
        model = Vendor
        fields = [
            "id", "name", "image", "website_url","description",
            "category", "category_id",
            "created_at", "updated_at"
        ]





class ProductMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "ram_gb", "price", "image")



class ProcessorSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(
        queryset=Vendor.objects.all(), source="vendor", write_only=True
    )

    products = ProductMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Processor
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    processor = ProcessorSerializer(read_only=True)
    processor_id = serializers.PrimaryKeyRelatedField(
        queryset=Processor.objects.all(), source="processor", write_only=True
    )


    class Meta:
        model = Product
        fields = "__all__"
