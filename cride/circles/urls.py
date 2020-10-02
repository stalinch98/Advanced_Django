"""Circles URLs."""
# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import circles as circles_views
from ..circles.views import memberships as membership_views

router = DefaultRouter()
router.register(r'circles', circles_views.CircleViewSet, basename='circle')
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-0_]+)/members',
    membership_views.MembershipViewSet,
    base_name='membership'
)

urlpatterns = [
    path('', include(router.urls))
]
