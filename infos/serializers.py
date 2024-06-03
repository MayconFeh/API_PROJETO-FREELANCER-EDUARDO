from rest_framework import serializers
from django.utils import timezone
from .models import Info


class InfoSerializer(serializers.ModelSerializer):
    area_de_atuacao = serializers.SerializerMethodField()
    visualizado = serializers.BooleanField(default=False)

    def get_area_de_atuacao(self, obj):
        return obj.activity.area_de_atuacao if obj.activity else None

    class Meta:
        model = Info
        fields = ('id', 'nome', 'endereco', 'area_de_atuacao', 'telefone', 'pdf', 'created_at', 'updated_at', 'deleted_at', 'is_deleted', 'visualizado')
        read_only_fields = ('id', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')
        extra_kwargs = {
            'pdf': {'required': True},
            'deleted_at': {'required': False},
            'is_deleted': {'required': False},
        }

    def create(self, validated_data):
        validated_data['created_at'] = timezone.now()
        validated_data['updated_at'] = timezone.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['updated_at'] = timezone.now()
        return super().update(instance, validated_data)
