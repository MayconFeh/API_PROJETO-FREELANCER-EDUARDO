from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("user/", views.UserListCreateView.as_view(), name='user-list-create'),
    path("user/<uuid:id>/", views.UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
