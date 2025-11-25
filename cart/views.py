# apps/cart/views.py
import uuid
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from product.models import Product
from .serializers import CartSerializer, CartItemSerializer


def get_or_create_cart(request):
    """
    Helper: Either get user's cart or guest cart using token.
    """
    user = request.user if request.user.is_authenticated else None
    cart_token = request.headers.get("X-Cart-Token")

    if user:
        cart, _ = Cart.objects.get_or_create(user=user, checked_out=False)
    else:
        if not cart_token:
            cart_token = str(uuid.uuid4())
        cart, _ = Cart.objects.get_or_create(cart_token=cart_token, checked_out=False)
    return cart, cart_token


class AddToCartView(APIView):
    """
    Add a product to cart with default quantity=1
    """
    def post(self, request, product_id):
        cart, cart_token = get_or_create_cart(request)
        product = get_object_or_404(Product, id=product_id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product,
            defaults={"quantity": 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        serializer = CartSerializer(cart)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        if not request.user.is_authenticated:
            response["X-Cart-Token"] = cart_token
        return response


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer

class CartListView(APIView):
    """
    Get all cart items with product details
    """
    def get(self, request):
        cart, cart_token = get_or_create_cart(request)
        
        # Pass request in context for absolute URLs
        serializer = CartSerializer(cart, context={"request": request})
        
        response = Response(serializer.data)
        if not request.user.is_authenticated:
            response["X-Cart-Token"] = cart_token
        return response


class CartItemUpdateView(generics.UpdateAPIView):
    """
    Update quantity of a cart item
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = "id"


class CartItemDeleteView(generics.DestroyAPIView):
    """
    Remove item from cart
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = "id"
