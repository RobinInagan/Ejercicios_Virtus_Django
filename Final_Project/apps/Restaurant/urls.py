from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Restaurant',RestaurantViewSet,basename='Restaurant')
router.register(r'Product',ProductViewSet,basename='Product')
router.register(r'Products_Restaurant',Products_RestaurantViewSet,basename='Products_Restaurant')


urlpatterns = [
]

urlpatterns += router.urls