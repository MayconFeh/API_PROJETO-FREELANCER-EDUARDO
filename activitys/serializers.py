from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'area_de_atuacao', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')
        read_only_fields = ('id', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')
