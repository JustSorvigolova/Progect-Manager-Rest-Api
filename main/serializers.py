from rest_framework import serializers
from .models import Projects, Tasks, Comments


class CommentCreateSerializer(serializers.ModelSerializer):
    """Комментарий"""

    class Meta:
        model = Comments
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """Задачи"""
    class Meta:
        model = Tasks
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    """Все проекты"""
    start = serializers.DateField()
    end = serializers.DateField()
    image_project = serializers.ImageField(allow_empty_file=True, use_url=True)
    comment = CommentCreateSerializer(many=True, read_only=True)
    task = TaskSerializer(many=True, read_only=True)

    def validate_date(self, data):
        if self.start > self.end:
            raise serializers.ValidationError("Дата окончания не может быть меньше начала даты")
        return data

    class Meta:
        model = Projects
        fields = "__all__"
