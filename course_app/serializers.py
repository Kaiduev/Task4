from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description',
                  'category', 'logo',
                  'contacts', 'branches']

    def create(self, validated_data):
        return Course.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'imgpath']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'latitude', 'longitude', 'address']

    def create(self, validated_data):
        return  Branch.objects.create(**validated_data)