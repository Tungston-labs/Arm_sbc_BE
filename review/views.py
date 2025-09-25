from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

# List all reviews for a specific product
class ProductReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Review.objects.filter(product_id=product_id, approved=True).order_by('-created_at')


# Add a review to a product
class ProductReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs['product_id'])
