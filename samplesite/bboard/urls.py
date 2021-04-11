from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    index,
    get_by_rubric_id,
    get_by_rubric_id_rest,
    APIRubricViewSet,
    ProfileAPI,
    # ProfileViewSet,
)

router = DefaultRouter()
router.register('rubric', APIRubricViewSet)
# router.register('profile', ProfileViewSet)

urlpatterns = [
    path('', index),
    path('rubric/<int:rubric_id>', get_by_rubric_id),
    path('rubric/<int:rubric_id>', get_by_rubric_id),
    path('api/rubric/<int:rubric_id>', get_by_rubric_id_rest),
    # path('api/rubric', APIRubric.as_view()),
    path('api/profiles', ProfileAPI.as_view()),
    path('api/', include(router.urls)),
]