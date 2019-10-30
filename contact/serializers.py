from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Serializer for Contact object"""

    class Meta:
        model = Contact
        fields = (
            "contact_type",
            "value"
        )
