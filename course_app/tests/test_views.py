# import json
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient, RequestsClient, APIRequestFactory
# from django.urls import path, include
# from course_app.models import *
#
#
# class CourseRequestsTestCase(APITestCase):
#
#     def test_course_get(self):
#         print("Test GET")
#         client = RequestsClient()
#         url = 'http://testserver/courses/'
#         response = client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_course_post(self):
#         print("setup post")
#         client = APIClient()
#         url = 'http://testserver/courses/'
#         self.category = Category.objects.create(name='Swimming', imgpath='lol.com')
#         self.branch = Branch.objects.create(latitude='12', longitude='21', address='Bishkek')
#         data = {
#             'name': 'English',
#             'description': 'some text',
#             'category': self.category.id,
#             'logo': 'some logo',
#             'contacts': [
#                 {'contact_type': 'FACEBOOK', 'value': 'weiuhwiuf'},
#                 {'contact_type': 'EMAIL', 'value': 'example@email.com'}
#             ],
#             'branches': [
#                 {'latitude': '2345678', 'longitude': '2345678765', 'address': 'soma alue'}
#             ],
#         }
#         response = client.post(url, data=data)
#         body = response.json()
#         print(body)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#
# class CategoryRequestsTestCase(APITestCase):
#
#     def test_categories_get(self):
#         print("Test Get categories")
#         client = RequestsClient()
#         url = 'http://testserver/categories/'
#         response = client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_category_post(self):
    #     print("Post category")
    #     url = 'http://testserver/categories/'
    #     client = RequestsClient()
    #     data = {'name': 'Languages', 'imgpath': 'someimg'}
    #     response = client.post(url, data)
    #     self.assertEquals(response.status_code, status.HTTP_201_CREATED)



