from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.transaction import atomic

from rest_framework.parsers import MultiPartParser, FormParser

from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.http import JsonResponse, HttpResponseForbidden

from .models import Items
from .serializers import ItemsSerializer

# @receiver(post_delete)
# def post_delete_dispatcher(sender, **kwargs):
#     print(kwargs['instance'].content_items)


def create_root_folder():
    object_for_save = {
        'name': 'Files',
        'type': 'FOLDER',
        'content_items': [],
        'is_root': True
    }
    serializer = ItemsSerializer(data=object_for_save)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


# def delete_root_by_id(root_id):
#     item = Items.objects.get(id_=root_id)
#     item.is_deleted = True
#     item.save()
#
#     serializer = ItemsSerializer(item)
#
#     return serializer.data


@api_view(['POST'])
def create_folder(request):
    parent_id = request.data.get('parent')
    name = request.data.get('name')
    object_for_save = {
        'name': name,
        'parent': parent_id,
        'type': 'FOLDER',
        'content_items': []
    }
    serializer = ItemsSerializer(data=object_for_save)

    if serializer.is_valid():
        serializer.save()
        #  DO WITH TRANSACTIONS
        parent = Items.objects.get(id=parent_id)
        parent.content_items.add(serializer.data.get('id'))
        parent.save()

        return JsonResponse(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    else:
        return JsonResponse(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def create_file(request):
    parent_id = request.data.get('parent')
    name = request.data.get('name')
    file = request.data.get('file')

    object_for_save = {
        'name': name,
        'parent': parent_id,
        'type': 'FILE',
        'file': file,
    }
    serializer = ItemsSerializer(data=object_for_save)

    if serializer.is_valid():
        serializer.save()
        #  DO WITH TRANSACTIONS
        parent = Items.objects.get(id=parent_id)
        parent.content_items.add(serializer.data.get('id'))
        parent.save()

        return JsonResponse(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    else:
        return JsonResponse(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_folder_content(request, folder_id):
    folder = Items.objects.get(id=folder_id)
    content = folder.content_items.exclude(is_deleted=True)
    serializer = ItemsSerializer(content, many=True)

    return Response(serializer.data)


@api_view(['PUT'])
def update_name(request, id):
    new_name = request.data.get('name')
    item = Items.objects.get(id=id)
    item.name = new_name
    item.save()
    serializer = ItemsSerializer(item)

    return Response(serializer.data)


@api_view(['PUT'])
@atomic
def move_item(request, id):
    move_to_id = request.data.get('move_to_id')

    item = Items.objects.get(id=id)

    parent = item.parent
    new_content_items = parent.content_items.exclude(id=id)
    parent.content_items.set(new_content_items)
    parent.save()

    move_to_item = Items.objects.get(id=move_to_id)
    move_to_item.content_items.add(item)

    item.parent = move_to_item
    item.save()

    serializer = ItemsSerializer(item)

    return Response(serializer.data)


class ItemsAPI(APIView):
    @staticmethod
    def get(request):
        content = Items.objects.all()
        serializer = ItemsSerializer(content, many=True)

        return Response(serializer.data)

    @staticmethod
    def delete(request):
        ids = request.data.get('ids')

        for_del = Items.objects.filter(id__in=ids)
        is_root = None

        try:
            is_root = for_del.get(is_root=True)
        except ObjectDoesNotExist:
            pass

        if is_root is not None:
            return JsonResponse(
                'Not allowed to perform this operation',
                status=status.HTTP_403_FORBIDDEN,
                safe=False
            )
        for item in for_del:
            item.is_deleted = True
            item.save()

        serializer = ItemsSerializer(for_del, many=True)

        return Response(serializer.data)
