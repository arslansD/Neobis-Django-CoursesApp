from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .models import Courses
from .serializers import CourseSerializers


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
