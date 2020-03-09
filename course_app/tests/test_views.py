import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, RequestsClient, APIRequestFactory
from django.urls import path, include
from course_app.models import *


class CourseRequestsTestCase(APITestCase):

    def test_course_get(self):
        print("Test GET")
        client = RequestsClient()
        url = 'http://testserver/courses/'
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_post(self):
        print("setup post")
        client = APIClient()
        url = 'http://testserver/courses/'
        self.category = Category.objects.create(name='Swimming', imgpath='lol.com')
        data = {
            'name': 'Python',
            'description': 'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics',
            'category': self.category.pk,
            'logo': 'some logo'
        }
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CourseDetailTestCase(APITestCase):

    def test_course_get(self):
        print("Test CourseDetail Get")
        self.category = Category.objects.create(name="Technical", imgpath="ImgPath")
        self.course = Course.objects.create(
            name='Python',
            description='Sample text',
            category=self.category,
            logo='Logo',
        )
        url = 'http://testserver/courses/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_put(self):
        print("Test CourseDetail put")
        self.category = Category.objects.create(name="Technical", imgpath="ImgPath")
        self.course = Course.objects.create(
            name='Python',
            description='Sample text',
            category=self.category,
            logo='Logo',
        )
        url = 'http://testserver/courses/1/'
        response = self.client.get(url)
        factory = APIRequestFactory()
        response_put = factory.post('http://testserver/courses/1/', {'name': 'Java',
                                                                'description': 'Samplel Text'})


class CategoryRequestsTestCase(APITestCase):

    def test_categories_get(self):
        print("Test Get categories")
        client = RequestsClient()
        url = 'http://testserver/categories/'
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_post(self):
        print("Post category")
        url = 'http://testserver/categories/'
        client = RequestsClient()
        data = {'name': 'Languages', 'imgpath': 'someimg'}
        response = client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class CategoryDetailTestCase(APITestCase):

    def test_category_detail(self):
        print("Test get category detail")
        self.category = Category.objects.create(name="Technical", imgpath="ImgPath")
        url = 'http://testserver/categories/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)





