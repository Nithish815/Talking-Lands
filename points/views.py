from rest_framework import generics
from .models import Point
from .serializers import PointSerializer

# Create and List Points
class PointListCreateView(generics.ListCreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

# Retrieve, Update, and Delete Point by ID
class PointRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    lookup_field = 'id'
