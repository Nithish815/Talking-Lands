from django.urls import path
from .views import PointListCreateView, PointRetrieveUpdateDeleteView

urlpatterns = [
    path('points/', PointListCreateView.as_view(), name='point-list-create'),
    path('points/<int:id>/', PointRetrieveUpdateDeleteView.as_view(), name='point-retrieve-update-delete'),
]
