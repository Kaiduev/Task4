# imports for model tests
from django.test import TestCase
from course_app.models import *


# Models tests CategoryTestsCase, CourseTestCase, BranchTestCase


class CategoryTestCase(TestCase):
    # Category Test
    def setUp(self):
        print('Setup Category Activity')
        self.category = Category.objects.create(name='Swimming', imgpath='lol.com')

    def test_category_into(self):
        self.assertEqual(self.category.name, 'Swimming')


class CourseTestCase(TestCase):
    # Course Test
    def setUp(self):
        print('Setup Course Activity')
        self.category = Category.objects.create(name="Technical", imgpath="ImgPath")
        self.course = Course.objects.create(
            name='Python',
            description='Sample text',
            category=self.category,
            logo='Logo',
        )

    def test_course_into(self):
        self.assertEqual(self.course.name, 'Python')


class BranchTestCase(TestCase):
    def setUp(self):
        print("Setup Branch Activity")
        self.category = Category.objects.create(name="Technical", imgpath="ImgPath")
        self.course = Course.objects.create(
            name='Python',
            description='Sample text',
            category=self.category,
            logo='Logo',
        )
        self.branch = Branch.objects.create(course=self.course,latitude='12', longitude='21', address='Bishkek')

    def test_branch_into(self):
        self.assertEqual(self.branch.address, 'Bishkek')


class ContactTestCase(TestCase):
    def setUp(self):
        print("Setup Contact Activity")
        self.category = Category.objects.create(name="Technical", imgpath="ImgPath")
        self.course = Course.objects.create(
            name='Python',
            description='Sample text',
            category=self.category,
            logo='Logo',
        )
        self.contact = Contact.objects.create(course=self.course,
                                              content_type=Contact.CONTACT_CHOISES,
                                              value='05216846')

    def test_contact_info(self):
        self.assertEqual(self.contact.value, '05216846')

