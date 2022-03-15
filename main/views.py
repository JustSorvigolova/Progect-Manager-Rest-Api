from .serializers import ProjectsSerializer
from main.models import Projects
from rest_framework.response import Response
from rest_framework import generics


class ProjectList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = ProjectsSerializer(queryset, many=True)
        return Response({
            "data": serializer.data,
            "success": True
        })


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer




