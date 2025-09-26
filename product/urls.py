from django.urls import path
from .views import ProductListCreateView,ProductDetailUpdateView,RelatedProductsView,ProductPublicDetailView,ProductPublicListView

urlpatterns = [
    path('create/', ProductListCreateView.as_view(), name='product-create'),
    path('<uuid:id>/', ProductDetailUpdateView.as_view(), name='product-detail-update'),
    path('public/', ProductPublicListView.as_view(), name='product-public-list'),
    path('public/<uuid:id>/', ProductPublicDetailView.as_view(), name='product-public-detail'),
    path("<uuid:id>/related/", RelatedProductsView.as_view(), name="related-products"),
]
