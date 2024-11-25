from django.urls import path
from .views import (
    POIListCreateView,
    POIDetailView)

urlpatterns = [
    path('api/poi/', POIListCreateView.as_view(), name='poi-list'),
    path('api/poi/<int:pk>/', POIDetailView.as_view(), name='poi-detail'),
]