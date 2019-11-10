from rest_framework import serializers
from branch.models import Branch
from category.models import Category
from contact.models import Contact
from .models import Courses
from contact.serializers import ContactSerializer
from branch.serializers import BranchSerializer


class CourseSerializers(serializers.ModelSerializer):
    """Courses serializer"""
    contacts = ContactSerializer(
        many=True,
    )
    branches = BranchSerializer(
        many=True
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Courses
        fields = (
            "contacts",
            "branches",
            "name",
            "description",
            "category",
            "logo"
        )

    def create(self, validated_data):
        branches = validated_data.pop("branches")
        contact = validated_data.pop("contacts")
        course = Courses.objects.create(**validated_data)

        for branches in branches:
            Branch.objects.create(course=course, **branches)

        for contact in contact:
            Contact.objects.create(course=course, **contact)

        return course
