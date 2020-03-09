from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import resolve, reverse
from course_app.views import *


# class TestUrls(APITestCase):
#
#     def test_courses_url(self):
#         url = 'courses/'
#         self.assertEqual(resolve(url).view_name, CourseView)