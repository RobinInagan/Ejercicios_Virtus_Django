from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects',ProjectViewSet, basename='projects')
router.register(r'tasks',TasksViewSet, basename='task')
router.register(r'comments',CommentsViewSet, basename='comments')

urlpatterns = [
]

urlpatterns += router.urls