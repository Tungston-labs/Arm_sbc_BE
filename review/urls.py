from django.urls import path
from .views import ProductReviewListView, ProductReviewCreateView

urlpatterns = [
    path('<uuid:product_id>/reviews/', ProductReviewListView.as_view(), name='product-reviews'),
    path('<uuid:product_id>/reviews/add/', ProductReviewCreateView.as_view(), name='add-review'),
]
