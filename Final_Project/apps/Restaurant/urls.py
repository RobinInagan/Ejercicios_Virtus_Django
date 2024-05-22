from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'restaurant',RestaurantViewSet,basename='restaurant')
router.register(r'product',ProductViewSet,basename='product')
router.register(r'products_Restaurant',Products_RestaurantViewSet,basename='products_Restaurant')
router.register(r'table',TableViewSet,basename='table')
router.register(r'tables_Restaurant',Tables_RestaurantViewSet,basename='tables_Restaurant')
router.register(r'waiter',WaiterViewSet,basename='waiter')

urlpatterns = [
]

urlpatterns += router.urls