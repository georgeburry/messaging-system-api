from django.urls import path, include
from rest_framework.routers import DefaultRouter

from threads.viewsets import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
