from rest_framework import serializers
from .models import Category


class CategorySerializers(serializers.ModelSerializer):
    """Category Serializer"""

    class Meta:
        model = Category
        field = (
            "name",
            "imgpath"
        )
