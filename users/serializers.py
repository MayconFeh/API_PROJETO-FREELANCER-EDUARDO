from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'email': {'validators': [UniqueValidator(queryset=User.objects.all(), message="Email already registered.")]}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
