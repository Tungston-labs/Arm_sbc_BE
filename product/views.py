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

from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


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




