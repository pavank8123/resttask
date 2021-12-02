from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from .models import Location, Department, Category, SubCategory, SKUData


class LocationSerializer(serializers.ModelSerializer):
    # department = serializers.PrimaryKeyRelatedField(many=True, queryset=Department.objects.filter(location=location))

    class Meta:
        model = Location
        fields = ['name', 'description']


class DepartmentSerializer(serializers.ModelSerializer):
    # location = LocationSerializer(many=False, read_only=True)
    class Meta:
        model = Department
        fields = ['dep_name', 'location']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['cat_name', 'dept']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['sub_cat_name', 'category']


class SKUDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKUData
        fields = ['name', 'location', 'department', 'category', 'subcategory']