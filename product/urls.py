from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    VendorListCreateView, VendorDetailView, CategoryVendorListView,
    ProcessorListCreateView, ProcessorDetailView, VendorProcessorListView,
    ProductListCreateView, ProductDetailView, ProcessorProductListView,
    SoftwareVendorListView
)

urlpatterns = [

    # CATEGORY
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/<int:category_id>/vendors/", CategoryVendorListView.as_view(), name="category-vendors"),

    # VENDORS
    path("vendors/", VendorListCreateView.as_view(), name="vendor-list"),
    path("vendors/<int:pk>/", VendorDetailView.as_view(), name="vendor-detail"),
    path("vendors/<int:vendor_id>/processors/", VendorProcessorListView.as_view(), name="vendor-processors"),

    # PROCESSORS
    path("processors/", ProcessorListCreateView.as_view(), name="processor-list"),
    path("processors/<int:pk>/", ProcessorDetailView.as_view(), name="processor-detail"),
    path("processors/<int:processor_id>/products/", ProcessorProductListView.as_view(), name="processor-products"),

    # BOARDS
 
    path("vendors/software/", SoftwareVendorListView.as_view()),

    # PRODUCTS
    path("list/", ProductListCreateView.as_view(), name="product-list"),
    path("list/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
