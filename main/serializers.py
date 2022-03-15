from rest_framework import serializers
from .models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    """Все проекты"""
    supervisor = serializers.SlugRelatedField(slug_field='username', read_only=True)
    developers = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)
    start = serializers.DateField(read_only=True)
    end = serializers.DateField(read_only=True)
    image_project = serializers.ImageField(allow_empty_file=False, use_url=True)

    def validate_date(self, data):
        if self.end < self.start:
            raise serializers.ValidationError("Дата окончания не может быть меньше начала даты")
        return data

    class Meta:
        model = Projects
        fields = "__all__"


class ProjectsDetailSerializer(serializers.ModelSerializer):
    """Список проекта"""

    class Meta:
        model = Projects
        fields = "__all__"

