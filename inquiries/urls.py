from django.urls import path
from .views import ProductInquiryCreateView, ProductInquiryListView, ProductInquiryDetailView,DashboardAPIView

urlpatterns = [
    path("create/", ProductInquiryCreateView.as_view(), name="inquiry-create"),
    path("", ProductInquiryListView.as_view(), name="inquiry-list"),
    path("<uuid:pk>/", ProductInquiryDetailView.as_view(), name="inquiry-detail"),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard-api'),
]
