from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from shared.pagination import CustomPagination

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]  
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'processor__cpu', 'memory__technology']  


class ProductDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id' 

# ------------------Public list view
class ProductPublicListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny] 
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'processor__cpu', 'memory__technology']  

# -----------------Public detail view
class ProductPublicDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  
    lookup_field = 'id'  

# related product list

class RelatedProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        product_id = self.kwargs["id"]
        try:
            product = Product.objects.get(id=product_id, available=True)
        except Product.DoesNotExist:
            return Product.objects.none()

       
        qs = Product.objects.filter(
            Q(ram=product.ram) | Q(cores=product.cores),
            available=True
        ).exclude(id=product.id)

        if not qs.exists():
            qs = Product.objects.exclude(id=product.id).filter(available=True)

        return qs[:4]  
