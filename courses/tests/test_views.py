from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from courses.serializers import CourseSerializers
from .utils import create_category, create_courses
from courses.models import Courses


COURSES_URL = reverse("courses")


class TestCourseViews(TestCase):
    """Class for testing courses views"""
    def setUp(self) -> None:
        self.client = APIClient()

    def test_get_course(self):
        """Testing GET method"""
        category = create_category()
        courseF1 = create_courses(category=category)
        courseF2 = create_courses(category=category)
        response = self.client.get(COURSES_URL)

        courses = Courses.objects.all()
        serializer = CourseSerializers(courses, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_course(self):
        """Testing POST method"""
        category = create_category()
        payload = {
            "name": "English courses",
            "description": "random stuff",
            "logo": "Other random stuff",
            "category": 1,
            "branches": [
                {
                    "longitude": "random longitude",
                    "latitude": "random latitude",
                    "address": "random address"
                }
            ],
            "contacts": [
                {
                    "contact_type": 1,
                    "value": 123
                }
            ]
        }

        response = self.client.post(COURSES_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        exists = Courses.objects.filter(name=response.data["name"]).exists()
        self.assertTrue(exists)

    def test_course_detail_get(self):
        """Testing GET method on detail of a course"""
        category = create_category()
        courses = create_courses(category=category)
        response = self.client.get(
            courses.get_url()
        )
        serializer = CourseSerializers(courses)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_course_detail_delete(self):
        """Testing DELETE method on course detail"""
        category = create_category(name="Intended course")
        courses = create_courses(category=category)
        response = self.client.delete(
            courses.get_url()
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        exists = Courses.objects.filter(name="Intended course")
        self.assertFalse(exists)
