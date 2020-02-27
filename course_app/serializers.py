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