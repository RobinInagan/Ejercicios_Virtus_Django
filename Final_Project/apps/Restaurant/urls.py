from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Restaurant',RestaurantViewSet,basename='Restaurant')

urlpatterns = [
]

urlpatterns += router.urls