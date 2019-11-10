from django.test import TestCase
from courses.models import Courses
from branch.models import Branch
from category.models import Category
from contact.models import Contact
from .utils import create_courses, create_category, create_branch, create_contact


class CoursesTest(TestCase):
    """Testing Courses models"""

    def test_category_creation(self):
        c = create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertTrue(str(c), c.name)

    def test_courses_creation(self):
        w = create_courses(category=create_category())
        self.assertTrue(isinstance(w, Courses))
        self.assertEqual(str(w), w.name)

    def test_branch_creation(self):
        b = create_branch(course=create_courses(category=create_category()))
        self.assertTrue(isinstance(b, Branch))
        self.assertEqual(str(b), b.address)

    def test_contact_creation(self):
        con = create_contact(course=create_courses(category=create_category()))
        self.assertTrue(isinstance(con, Contact))
        self.assertEqual(str(con), con.value)

