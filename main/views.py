from .serializers import ProjectsSerializer, CommentCreateSerializer, UserSerializer
from main.models import Projects, Comment
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User


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


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
