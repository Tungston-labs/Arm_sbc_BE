from django.urls import path
from .views import AddToCartView, CartListView, CartItemUpdateView, CartItemDeleteView

urlpatterns = [
    path("", CartListView.as_view(), name="cart-list"),
    path("add/<int:product_id>/", AddToCartView.as_view(), name="cart-add"),
    path("item/<uuid:id>/update/", CartItemUpdateView.as_view(), name="cartitem-update"),
    path("item/<uuid:id>/delete/", CartItemDeleteView.as_view(), name="cartitem-delete"),
]
