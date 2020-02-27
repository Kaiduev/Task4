from django.urls import path, include
from . import views


app_name = 'course_app'

urlpatterns = [
    path('courses/',views.CourseView.as_view()),
    path('courses/<int:pk>/',views.CourseDetail.as_view()),
]