from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.transaction import atomic
from django.db import IntegrityError

from .models import Projects
from finder.views import create_root_folder
from .serializers import ProjectsSerializer


class ProjectsAPI(APIView):
    @staticmethod
    def get(request):
        data = Projects.objects.all()

        serializer = ProjectsSerializer(data, many=True)
        return Response(serializer.data)

    @atomic
    def post(self, request):
        name = request.data.get('name')
        root_folder = create_root_folder()
        object_for_save = {
            'name': name,
            'root_folder': root_folder.get('pk'),
            'is_deleted': False
        }
        # fix: do not work atomic
        try:
            with atomic():
                serializer = ProjectsSerializer(data=object_for_save)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        serializer.data,
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except IntegrityError:
            print('errororroor')  # this will run after rollback


    @staticmethod
    def put(request):
        name = request.data.get('name')
        id = request.data.get('id')

        project = Projects.objects.get(id=id)
        project.name = name;
        project.save()

        serializer = ProjectsSerializer(project)
        return Response(serializer.data)

    @staticmethod
    def delete(request):
        id = request.data.get('id')
        project = Projects.objects.get(id=id)
        related_root_folder = project.root_folder

        project.is_deleted = True
        project.save()

        related_root_folder.is_deleted = True
        related_root_folder.save()

        return Response({})

