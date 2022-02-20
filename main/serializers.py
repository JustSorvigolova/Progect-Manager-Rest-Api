from rest_framework import serializers

from .models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    """Список проектов"""

    class Meta:
        model = Projects
        field = ("title")




