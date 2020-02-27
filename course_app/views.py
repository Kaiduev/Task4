from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from . import serializers
from rest_framework import status


class CourseView(APIView):

    serializer_class = serializers.CourseSerializer

    def get(self, request):
        courses = Course.objects.all()
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response({"courses": serializer.data})

    def post(self,request):
        serializer = serializers.CourseSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success": "Course '{}' created successfully".format(saved_data.name)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):

    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = serializers.CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        Resp = Course.objects.get(pk=pk)
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({"success": "Course '{}' was deleted".format(Resp.name)}, status=status.HTTP_204_NO_CONTENT)