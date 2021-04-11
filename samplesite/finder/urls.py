from django.urls import path, include

from .views import (
    ItemsAPI,
    create_folder,
    get_folder_content,
    update_name,
    move_item,
    create_file,
)


urlpatterns = [
    path('items', ItemsAPI.as_view()),
    path('folder', create_folder),
    path('item', create_file),
    path('folder/content/<int:folder_id>', get_folder_content),
    path('item/<int:id>', update_name),
    path('item/move/<int:id>', move_item),
]
