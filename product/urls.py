from django.urls import path
from .views import (
    ProductListCreateView,
    ProductDetailUpdateView,
    RelatedProductsView,
    ProductPublicDetailView,
    ProductPublicListView,
)
from .views_catalog import CatalogView


urlpatterns = [
    # Admin create/list
    path("create/", ProductListCreateView.as_view(), name="product-create"),

    # Admin detail/update
    path("<uuid:idx>/", ProductDetailUpdateView.as_view(), name="product-detail-update"),

    # Public list + detail
    path("public/", ProductPublicListView.as_view(), name="product-public-list"),
    path("public/<uuid:idx>/", ProductPublicDetailView.as_view(), name="product-public-detail"),

    # Related products
    path("<uuid:idx>/related/", RelatedProductsView.as_view(), name="related-products"),

    # NEW — SoC + Board Catalog
    path("catalog/", CatalogView.as_view(), name="product-catalog"),
]

