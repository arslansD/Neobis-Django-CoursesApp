from django.db import models


class Category(models.Model):
    """Model category"""
    name = models.CharField(max_length=255)
    imgpath = models.CharField(max_length=255)

    def __str__(self):
        return self.name
