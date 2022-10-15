from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Todo
        fields = ["id", 'title', 'description',
                  'completed', 'created_at']
