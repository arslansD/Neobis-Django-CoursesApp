from django.db import models
from django.urls import reverse

from category.models import Category


class Courses(models.Model):
    """Courses model"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("courses-detail", kwargs={"pk": self.pk})
