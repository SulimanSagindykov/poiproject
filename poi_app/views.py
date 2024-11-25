from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import PointOfInterest
from .serializers import PointOfInterestSerializer

class POIListCreateView(generics.ListCreateAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
    filterset_fields = ['category']

class POIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer