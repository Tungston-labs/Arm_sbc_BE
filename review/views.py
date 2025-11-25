from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from django.db.models import Avg, Count


class ProductReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Review.objects.filter(product_id=product_id, approved=True).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        
        stats = queryset.aggregate(
            total_reviews=Count('id'),
            avg_rating=Avg('rating')
        )

        data = {
            "total_reviews": stats["total_reviews"] or 0,
            "avg_rating": round(stats["avg_rating"], 2) if stats["avg_rating"] else 0,
            "max_rating": 5,  
            "reviews": serializer.data
        }
        return Response(data)

# Add a review to a product
class ProductReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs['product_id'])
