from django.urls import path, include 
from .api_app_views import ShoppingCart


urlpatterns = [
    path('cart-items/', ShoppingCart.as_view()),
    
]