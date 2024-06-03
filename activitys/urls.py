from django.urls import path
from .views import ActivityListCreateView, ActivityRetrieveUpdateDestroyView

urlpatterns = [
    path('activities/', ActivityListCreateView.as_view(), name='activity-list-create'),
    path('activities/<uuid:ac_id>/', ActivityRetrieveUpdateDestroyView.as_view(), name='activity-detail'),
]
