from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Restaurant',RestaurantViewSet,basename='Restaurant')
router.register(r'Product',ProductViewSet,basename='Product')
router.register(r'Products_Restaurant',Products_RestaurantViewSet,basename='Products_Restaurant')
router.register(r'Table',TableViewSet,basename='Table')
router.register(r'Tables_Restaurant',Tables_RestaurantViewSet,basename='Tables_Restaurant')

urlpatterns = [
]

urlpatterns += router.urls