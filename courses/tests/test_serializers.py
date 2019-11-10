from django.test import TestCase
from .utils import create_category
from courses import serializers, models


class TestCourseSerializers(TestCase):
    """Class for testing course serializers"""
    def test_custom_create(self):
        category = create_category()
        course_dictionary = {
            "name": "Random course name",
            "description": "Random text",
            "logo": "random logo",
            "category": 1,
            "branches": [
                {
                    "longitude": "random",
                    "latitude": "random",
                    "address": "random address"
                }
            ],
            "contacts": [
                {
                    "contact_type": 1,
                    "value": "random"
                }
            ]
        }
        serializer = serializers.CourseSerializers(data=course_dictionary)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        exists = models.Courses.objects.get(id=1)
        self.assertIsNotNone(exists)
