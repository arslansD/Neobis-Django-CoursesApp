from courses.models import Courses
from category.models import Category
from branch.models import Branch
from contact.models import Contact


def create_category(name="Checking", imgpath="also checking"):
    return Category.objects.create(name=name, imgpath=imgpath)


def create_courses(name="only a test", description="yes, this is only a test", logo="Check", category=None):
    return Courses.objects.create(name=name, description=description, logo=logo, category=category)


def create_branch(latitude="yeah, another one", longitude="and another one", address="another one", course=None):
    return Branch.objects.create(latitude=latitude, longitude=longitude, address=address, course=course)


def create_contact(contact_type=1, value="Any value", course=None):
    return Contact.objects.create(contact_type=contact_type, value=value, course=course)
