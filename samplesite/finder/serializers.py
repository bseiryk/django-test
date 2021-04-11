from rest_framework import serializers
from .models import Items


class ItemsSerializer(serializers.ModelSerializer):
    file = serializers.FileField(
        max_length=None,
        use_url=True
    )

    class Meta:
        model = Items
        fields = ('id', 'pk', 'name', 'file', 'parent', 'is_root', 'type', 'content_items')
