# imports for model tests
from django.test import TestCase
from .models import *

# imports for view tests

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, RequestsClient, APIRequestFactory
from django.urls import path, include


# Models tests CategoryTestsCase and CourseTestCase


class CategoryTestCase(TestCase):
    # Category Test
    def setUp(self):
        print('.Setup Category Activity')
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
            contacts=Contact.CONTACT_CHOISES
        )

    def test_course_into(self):
        self.assertEqual(self.course.name, 'Python')


class GetRequestTestCase(APITestCase):

    def test_course_get(self):
        print("Test GET")
        client = RequestsClient()
        url = 'http://testserver/courses/'
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_post(self):
        data = {'Name': 'Python', 'Description': 'sometext',
                'Category': 'Technical', 'Logo': 'logo', 'Contacts': 'Phone',
                'Branches': 'Latitude'}

        client = APIClient()
        response = client.post('/courses/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
