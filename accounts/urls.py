from django.urls import path
from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]