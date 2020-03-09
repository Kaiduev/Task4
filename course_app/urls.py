from django.urls import path, include
from django.conf.urls import url
from . import views


app_name = 'course_app'

urlpatterns = [
    path('courses/',views.CourseView.as_view()),
    path('courses/<int:pk>/',views.CourseDetail.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('contacts/', views.ContactsView.as_view()),
    path('branches/', views.BranchView.as_view()),
]