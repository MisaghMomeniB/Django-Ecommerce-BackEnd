from django.urls import path
from .views import ProtectedTestView
from .views import CartView
from .views import CreateOrderView, UserOrdersListView, PayOrderView
from .views import product_list, product_detail, add_to_cart, view_cart, checkout

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('protected/', ProtectedTestView.as_view(), name='protected'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CreateOrderView.as_view(), name='checkout'),
    path('orders/', UserOrdersListView.as_view(), name='user-orders'),
    path('orders/<int:order_id>/pay/', PayOrderView.as_view(), name='pay-order'),
]