from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from shared.pagination import CustomPagination
from rest_framework import generics
from .models import Category, Vendor, Processor,  Product
from .serializers import (
    CategorySerializer,
    VendorSerializer,
    ProcessorSerializer,
    ProductSerializer,
)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class CategoryVendorListView(generics.ListAPIView):
    serializer_class = VendorSerializer

    def get_queryset(self):
        return Vendor.objects.filter(category_id=self.kwargs["category_id"])



class ProcessorListCreateView(generics.ListCreateAPIView):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer


class ProcessorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer


class VendorProcessorListView(generics.ListAPIView):
    serializer_class = ProcessorSerializer

    def get_queryset(self):
        return Processor.objects.filter(vendor_id=self.kwargs["vendor_id"])



from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from shared.pagination import CustomPagination

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination  
    
    def get_queryset(self):
        queryset = Product.objects.all()

        processor_id = self.request.query_params.get("processor_id")
        processor_name = self.request.query_params.get("processor_name")
        processor_code = self.request.query_params.get("processor_code")
        board_name = self.request.query_params.get("board_name")
        ram_gb = self.request.query_params.get("ram_gb")
        price_min = self.request.query_params.get("price_min")
        price_max = self.request.query_params.get("price_max")
        available = self.request.query_params.get("available")

        # ⭐ FILTER BY PROCESSOR ID (MOST IMPORTANT FIX)
        if processor_id:
            queryset = queryset.filter(processor_id=processor_id)

        # Filter by Processor fields
        if processor_name:
            queryset = queryset.filter(processor__name__icontains=processor_name)
        if processor_code:
            queryset = queryset.filter(processor__code__icontains=processor_code)

        # Filter by Board fields
        if board_name:
            queryset = queryset.filter(board__name__icontains=board_name)

        if ram_gb:
            queryset = queryset.filter(ram_gb=ram_gb)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        if available is not None:
            if available.lower() == "true":
                queryset = queryset.filter(available=True)
            elif available.lower() == "false":
                queryset = queryset.filter(available=False)

        return queryset


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SoftwareVendorListView(generics.ListAPIView):
    serializer_class = VendorSerializer

    def get_queryset(self):
        return Vendor.objects.filter(vendor_type="software")


class ProcessorProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(processor_id=self.kwargs["processor_id"])




