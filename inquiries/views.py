from rest_framework import generics
from .models import ProductInquiry
from .serializers import ProductInquirySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from product.models import Product
from rest_framework import generics, permissions
from shared.pagination import CustomPagination


class ProductInquiryCreateView(generics.CreateAPIView):
    queryset = ProductInquiry.objects.all()
    serializer_class = ProductInquirySerializer

class ProductInquiryListView(generics.ListAPIView):
    queryset = ProductInquiry.objects.all()
    serializer_class = ProductInquirySerializer
    pagination_class = CustomPagination


class ProductInquiryDetailView(generics.RetrieveUpdateAPIView):
    queryset = ProductInquiry.objects.all()
    serializer_class = ProductInquirySerializer


# dashboard counts



class DashboardAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]


    def get(self, request):
        new_inquiries_count = ProductInquiry.objects.filter(status='pending').count()
        total_products_count = Product.objects.count()

        data = {
            "new_inquiries_count": new_inquiries_count,
            "total_products_count": total_products_count
        }
        return Response(data)
