from django.urls import path
from .views import ProtectedTestView

urlpatterns = [
    path('protected/', ProtectedTestView.as_view(), name='protected'),
]