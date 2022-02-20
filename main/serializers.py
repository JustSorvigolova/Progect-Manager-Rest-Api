from rest_framework import serializers
from .models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    """Все проектов"""

    class Meta:
        model = Projects
        fields = '__all__'


class ProjectsDetailSerializer(serializers.ModelSerializer):
    """Список проектов"""
    workers = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    supervisor = serializers.SlugRelatedField(slug_field='name', read_only=True)
    admin = serializers.SlugRelatedField(slug_field='name', read_only=True)
    task = serializers.SlugRelatedField(slug_field='task', read_only=True)

    class Meta:
        model = Projects
        fields = '__all__'
