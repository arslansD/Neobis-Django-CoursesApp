from rest_framework import serializers
from .models import Branch


class BranchSerializer(serializers.ModelSerializer):
    """Serializers for Branch"""

    class Meta:
        model = Branch
        fields = (
            "latitude",
            "longitude",
            "address"
        )
