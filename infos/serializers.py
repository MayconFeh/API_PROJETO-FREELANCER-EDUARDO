from rest_framework import serializers
from .models import Info, Activity
from django.utils import timezone


class InfoSerializer(serializers.ModelSerializer):
    area_de_atuacao = serializers.CharField(source='area_de_atuacao.area_de_atuacao')
    visualizado = serializers.BooleanField(default=False)

    class Meta:
        model = Info
        fields = ('id', 'nome', 'endereco', 'area_de_atuacao', 'telefone', 'pdf', 'created_at', 'updated_at', 'deleted_at', 'is_deleted', 'visualizado')
        read_only_fields = ('id', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')
        extra_kwargs = {
            'pdf': {'required': False},
            'deleted_at': {'required': False},
            'is_deleted': {'required': False},
        }

    def create(self, validated_data):
        activity_name = validated_data.pop('area_de_atuacao')['area_de_atuacao']
        activity = Activity.objects.get(area_de_atuacao=activity_name)
        validated_data['area_de_atuacao'] = activity
        validated_data['created_at'] = timezone.now()
        validated_data['updated_at'] = timezone.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'area_de_atuacao' in validated_data:
            activity_name = validated_data.pop('area_de_atuacao')['area_de_atuacao']
            activity = Activity.objects.get(area_de_atuacao=activity_name)
            validated_data['area_de_atuacao'] = activity
        validated_data['updated_at'] = timezone.now()
        return super().update(instance, validated_data)
