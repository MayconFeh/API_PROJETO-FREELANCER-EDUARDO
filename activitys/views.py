from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAuthenticatedAndAdminOrOwner
from .models import Activity
from .serializers import ActivitySerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.utils import timezone


@extend_schema_view(
    get=extend_schema(
        description="Rota para listar todas as áreas de atuação",
        tags=["Listagem de Áreas de Atuação"],
        responses={200: ActivitySerializer(many=True)},
    ),
    post=extend_schema(
        description="Rota para criação de uma área de atuação",
        tags=["Criação de Áreas de Atuação"],
        request=ActivitySerializer,
        responses={201: ActivitySerializer},
    )
)
class ActivityListCreateView(ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedAndAdminOrOwner]

    def perform_create(self, serializer):
        serializer.save()


@extend_schema_view(
    get=extend_schema(
        description="Rota para pesquisa de uma área de atuação",
        tags=["Área de Atuação"],
        responses={200: ActivitySerializer}
    ),
    put=extend_schema(
        description="Rota para atualização de uma área de atuação",
        tags=["Área de Atuação"],
        request=ActivitySerializer,
        responses={200: ActivitySerializer}
    ),
    delete=extend_schema(
        description="Rota para deleção de uma área de atuação",
        tags=["Área de Atuação"],
        responses={204: None}
    )
)
class ActivityRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedAndAdminOrOwner]
    lookup_field = 'id'

    def get_object(self):
        ac_id = self.kwargs['ac_id']
        return Activity.objects.get(id=ac_id)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.deleted_at = timezone.now()
        instance.is_deleted = True
        instance.save()
