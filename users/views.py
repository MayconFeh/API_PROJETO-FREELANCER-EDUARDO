from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
from .models import User
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated


@extend_schema_view(
    get=extend_schema(
        description="Rota para listar todos os usuários",
        tags=["Listagem de Usuários"],
        responses={200: UserSerializer(many=True)},
    ),
    post=extend_schema(
        description="Rota para criação de usuários",
        tags=["Criação de Usuários"],
        request=UserSerializer,
        responses={201: UserSerializer},
    )
)
class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@extend_schema_view(
    get=extend_schema(
        description="Rota para pesquisa de um usuário",
        tags=["Usuário"],
        responses={200: UserSerializer}
    ),
    put=extend_schema(
        description="Rota para atualização de um usuário",
        tags=["Usuário"],
        request=UserSerializer,
        responses={200: UserSerializer}
    ),
    delete=extend_schema(
        description="Rota para deleção de um usuário",
        tags=["Usuário"],
        responses={204: None}
    )
)
class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
