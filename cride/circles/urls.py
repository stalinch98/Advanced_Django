"""Circles URLs."""
# Django
from django.urls import path

# Views
from cride.circles.views import list_circles
from cride.circles.views import create_circle

urlpatterns = [
    path('circles/', list_circles),
    path('circle/create', create_circle)
]
