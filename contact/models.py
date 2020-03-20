from django.db import models

from courses.models import Courses


class Contact(models.Model):
    """Contacts models"""
    PHONE = 1
    FACEBOOK = 2
    EMAIL = 3

    CONTACT_CHOICES = (
        (PHONE, "Phone"),
        (FACEBOOK, "Facebook"),
        (EMAIL, "Email")
    )
    contact_type = models.IntegerField(choices=CONTACT_CHOICES)
    value = models.CharField(max_length=255)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="contacts")

    def __str__(self):
        return self.value
