from rest_framework import serializers
from .models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    """Все проектов"""
    workers = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    task = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)

    class Meta:
        model = Projects
        fields = '__all__'


class ProjectsDetailSerializer(serializers.ModelSerializer):
    """Список проектов"""
    workers = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    task = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)

    class Meta:
        model = Projects
        fields = '__all__'
