from django.urls import path
from .views import InfoListCreateView, InfoRetrieveUpdateDestroyView

urlpatterns = [
    path('infos/', InfoListCreateView.as_view(), name='info-list-create'),
    path('infos/<uuid:id>/', InfoRetrieveUpdateDestroyView.as_view(), name='info-retrieve-update-destroy'),
]
