from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, MessageViewSet, FriendshipViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'message', MessageViewSet)
router.register(r'friendship', FriendshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
