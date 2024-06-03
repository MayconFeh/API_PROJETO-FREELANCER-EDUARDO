from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Info
from .serializers import InfoSerializer
from users.permissions import IsAuthenticatedAndAdminOrOwner
from django.utils import timezone


@extend_schema_view(
    get=extend_schema(
        description="Rota para listar todas as informações",
        tags=["Listagem de Informações"],
        responses={200: InfoSerializer(many=True)},
    ),
    post=extend_schema(
        description="Rota para criação de uma nova informação",
        tags=["Criação de Informações"],
        request=InfoSerializer,
        responses={201: InfoSerializer},
    )
)
class InfoListCreateView(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['area_de_atuacao', 'is_deleted']
    search_fields = ['nome', 'endereco', 'area_de_atuacao', 'telefone']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save()


@extend_schema_view(
    get=extend_schema(
        description="Rota para obter uma informação",
        tags=["Informação"],
        responses={200: InfoSerializer}
    ),
    put=extend_schema(
        description="Rota para atualização de uma informação",
        tags=["Informação"],
        request=InfoSerializer,
        responses={200: InfoSerializer}
    ),
    delete=extend_schema(
        description="Rota para deleção de uma informação",
        tags=["Informação"],
        responses={204: None}
    )
)
class InfoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedAndAdminOrOwner]
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.deleted_at = timezone.now()
        instance.is_deleted = True
        instance.save()
