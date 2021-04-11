from django.http import HttpResponse, JsonResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.gzip import gzip_page
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
import os

from .models import Bd, Rubric, Profile, Education
from .serializers import RubricSerializer, ProfileSerializer, BdSerializer


# @gzip_page
def index(request):
    p = Profile.objects.all()
    serializer = ProfileSerializer(p, many=True)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'assets/img.png')

    print(filename)

    # return FileResponse(open(filename, 'rb'))
    return JsonResponse(serializer.data,  safe=False)


def get_by_rubric_id(request, rubric_id):
    response = []
    items = Bd.objects.filter(rubric=rubric_id)
    for item in items:
        response.append(item.title)

    return HttpResponse(response, content_type='application/json')

# @api_view(['GET'])
def get_by_rubric_id_rest(request, rubric_id):
    items = Rubric.objects.filter(id=rubric_id)
    serializer = RubricSerializer(items, many=True)

    return JsonResponse(serializer.data, safe=False)


# class APIRubric(generics.CreateAPIView):
#     queryset = Rubric.objects.all()
#     serializer_class = RubricSerializer
    #
    # def post(self, request):
    #     serializer = RubricSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(
    #             serializer.data,
    #             status=status.HTTP_201_CREATED
    #         )
    #     else:
    #         return JsonResponse(
    #             serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST
    #         )


class APIRubricViewSet(ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


class ProfileAPI(APIView):
    @staticmethod
    def get(request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return JsonResponse(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

