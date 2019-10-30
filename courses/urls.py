from django.urls import path
from . import views


urlpatterns = [
    path(
        "courses/",
        view=views.CourseListView.as_view(),
        name="courses"
    ),
    path(
        "courses/<int:pk>/",
        view=views.CoursesDetailView.as_view(),
        name="courses-detail"
    )
]
