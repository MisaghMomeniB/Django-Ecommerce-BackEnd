from django.urls import path
from .views import ProtectedTestView
from .views import CartView

urlpatterns = [
    path('protected/', ProtectedTestView.as_view(), name='protected'),
    path('cart/', CartView.as_view(), name='cart'),
]