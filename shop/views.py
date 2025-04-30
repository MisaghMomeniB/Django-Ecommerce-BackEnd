from .models import Order, OrderItem, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem, Product
from .serializers import CartSerializer, AddToCartSerializer
from .models import Order, OrderItem, Cart, CartItem
from .serializers import OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

# Create your views here.
class ProtectedTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hi {request.user.username}, Done!"})
    
class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']

            cart, created = Cart.objects.get_or_create(user=request.user)
            product = Product.objects.get(id=product_id)

            item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                item.quantity += quantity
            else:
                item.quantity = quantity
            item.save()

            return Response({"message": "محصول به سبد اضافه شد."}, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        product_id = request.data.get('product_id')
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response({"error": "سبدی وجود ندارد"}, status=404)

        item = cart.items.filter(product_id=product_id).first()
        if item:
            item.delete()
            return Response({"message": "محصول از سبد حذف شد."})
        return Response({"error": "محصول در سبد پیدا نشد."}, status=404)
    
class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        cart = Cart.objects.filter(user=request.user).first()
        if not cart or not cart.items.exists():
            return Response({'error': 'سبد خرید خالی است'}, status=400)

        order = Order.objects.create(user=request.user)

        for item in cart.items.all():
                if item.quantity > item.product.stock:
                    return Response(
                        {"error": f"محصول '{item.product.name}' موجودی کافی ندارد."},
                        status=400
                    )
            
                for item in cart.items.all():
                     OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )
                item.product.stock -= item.quantity
                if item.product.stock == 0:
                    item.product.available = False
                item.product.save()

        # پاک کردن سبد خرید
        cart.items.all().delete()

        return Response({'message': 'سفارش ثبت شد'}, status=201)

class UserOrdersListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')
    
class PayOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        order = Order.objects.filter(id=order_id, user=request.user).first()
        if not order:
            return Response({"error": "سفارشی پیدا نشد"}, status=404)
        if order.is_paid:
            return Response({"message": "سفارش قبلاً پرداخت شده"}, status=400)

        # شبیه‌سازی پرداخت موفق
        order.is_paid = True
        order.save()

        return Response({"message": "پرداخت انجام شد"})
    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        item.quantity += quantity
        item.save()
    return redirect('cart')

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    return render(request, 'shop/cart.html', {'items': items})

from django.views.decorators.csrf import csrf_exempt

# @login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return redirect('cart')

    if request.method == 'POST':
        order = Order.objects.create(user=request.user)

        for item in cart.items.all():
            if item.quantity > item.product.stock:
                # برگرد به cart با پیغام خطا (برای حالت UI)
                return redirect('cart')

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
            item.product.stock -= item.quantity
            if item.product.stock == 0:
                item.product.available = False
            item.product.save()

        cart.items.all().delete()
        return redirect('orders')  # تو باید صفحه orders رو هم ساخته باشی

    return render(request, 'shop/checkout.html')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user, is_paid=True),
    return render(request, 'shop/orders.html', {'orders': orders})