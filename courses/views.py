from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from .serializers import CourseSerializers
from .models import Courses


class CourseListView(ListCreateAPIView):
    """API view for list"""
    model = Courses
    queryset = Courses.objects.all()
    serializer_class = CourseSerializers


class CoursesDetailView(RetrieveDestroyAPIView):
    """API view for detail"""
    model = Courses
    queryset = Courses.objects.all()
    serializer_class = CourseSerializers
