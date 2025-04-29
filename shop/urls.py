from django.urls import path
from .views import ProtectedTestView
from .views import CartView
from .views import CreateOrderView, UserOrdersListView, PayOrderView

urlpatterns = [
    path('protected/', ProtectedTestView.as_view(), name='protected'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CreateOrderView.as_view(), name='checkout'),
    path('orders/', UserOrdersListView.as_view(), name='user-orders'),
    path('orders/<int:order_id>/pay/', PayOrderView.as_view(), name='pay-order'),
]