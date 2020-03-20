from django.db import models

from courses.models import Courses


class Branch(models.Model):
    """Model branch"""
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="branches")

    def __str__(self):
        return self.address
