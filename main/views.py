from rest_framework.response import Response
from  rest_framework.views import APIView


from .models import Projects

from .serializers import ProjectsSerializer


class ProjectsListView(APIView):

    def get(self,request):
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)


