from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, Category, Branch
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

    def put(self, request, pk, format=None):
        course = Course.objects.get(pk=pk)
        serializer = serializers.CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Resp = Course.objects.get(pk=pk)
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({"success": "Course '{}' was deleted".format(Resp.name)}, status=status.HTTP_204_NO_CONTENT)


class CategoryView(APIView):

    serializer_class = serializers.CategorySerializer

    def get(self, request):
        categories = Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response({"Categories": serializer.data})

    def post(self,request):
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success": "Category '{}' created successfully".format(saved_data.name)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):

    serializer_class = serializers.CategorySerializer

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = serializers.CategorySerializer(category)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        categories = Category.objects.get(pk=pk)
        serializer = serializers.CategorySerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Resp = Category.objects.get(pk=pk)
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({"success": "Category '{}' was deleted".format(Resp.name)}, status=status.HTTP_204_NO_CONTENT)


class BranchView(APIView):

    serializer_class = serializers.BranchSerializer

    def get(self, request):
        branches = Branch.objects.all()
        serializer = serializers.BranchSerializer(branches, many=True)
        return Response({"Branches": serializer.data})

    def post(self, request):
        serializer = serializers.BranchSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"success": "Branch '{}' created successfully".format(saved_data.address)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class BranchDetail(APIView):

    serializer_class = serializers.BranchSerializer

    def get(self,request, pk):
        branch = Branch.objects.get(pk=pk)
        serializer = serializers.BranchSerializer(branch)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        branch = Branch.objects.get(pk=pk)
        serializer = serializers.BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Resp = Branch.objects.get(pk=pk)
        branch = Branch.objects.get(pk=pk)
        branch.delete()
        return Response({"success": "Branch '{}' was deleted".format(Resp.address)}, status=status.HTTP_204_NO_CONTENT)

