from .serializers import ProjectsSerializer, CommentCreateSerializer, TaskSerializer
from main.models import Projects, Comment, Tasks
from rest_framework.response import Response
from rest_framework import generics


class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = ProjectsSerializer(queryset, many=True)
        return Response({
                "data": serializer.data,
                "success": True,
            })


class ProjectUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = CommentCreateSerializer(queryset, many=True)
        return Response({
            "data": serializer.data,
            "success": True,
        })


class TasksListCreate(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response({
            "data": serializer.data,
            "success": True,
        })


