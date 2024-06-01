from rest_framework import serializers
from .models import Info
from django.utils import timezone


class InfoSerializer(serializers.ModelSerializer):
    visualizado = serializers.BooleanField(default=False)  # Novo campo

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

    def delete(self, instance):
        instance.deleted_at = timezone.now()
        instance.is_deleted = True
        instance.save()
