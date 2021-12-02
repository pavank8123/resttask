from .models import Location, Department, Category, SubCategory, SKUData
from .serializers import LocationSerializer, DepartmentSerializer, CategorySerializer, SubCategorySerializer, SKUDataSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LocationList(APIView):
    """
    List all locations, or create a new location.
    """
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LocationDetail(APIView):
    """
    Retrieve, update or delete a location instance.
    """
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentList(APIView):
    """
    List all Department, or create a new one.
    """
    def get(self, request,pk1):
        locations = Department.objects.filter(location=pk1)
        serializer = DepartmentSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, pk1):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetail(APIView):
    """
    Retrieve, update or delete a Department instance.
    """

    def get_object(self, pk1,pk):
        try:
            return Department.objects.get(location=pk1,pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk1, pk):
        department = self.get_object(pk1,pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk1, pk):
        department = self.get_object(pk1,pk).first()
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk1, pk):
        department = self.get_object(pk1, pk).first()
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    """
    List all Categories, or create a new Category.
    """
    def get(self, request,locpk,deptpk):
        locations = Category.objects.filter(dept=deptpk, dept__location=locpk)
        serializer = CategorySerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request,locpk,deptpk):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    Retrieve, UPdate, or Delete Category instance.
    """

    def get_object(self, locpk, deptpk, pk):
        try:
            return Category.objects.filter(dept=deptpk, dept__location=locpk,pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, locpk, deptpk, pk):
        locations = self.get_object(locpk, deptpk, pk)
        serializer = CategorySerializer(locations, many=True)
        return Response(serializer.data)

    def put(self, request, locpk, deptpk, pk):
        location = self.get_object(locpk, deptpk, pk).first()
        serializer = CategorySerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, locpk, deptpk, pk):
        location = self.get_object(locpk, deptpk, pk).first()
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubCategoryList(APIView):
    """
    List all SubCategory, or create a new SubCategory
    """
    def get(self, request,locpk,deptpk, catpk):
        locations = SubCategory.objects.filter(category=catpk, category__dept=deptpk, category__dept__location=locpk)
        serializer = SubCategorySerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request,locpk,deptpk,catpk):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubCategoryDetail(APIView):
    """
    Retrieve, Update, Delete Sub Category instance.
    """

    def get_object(self, locpk, deptpk, catpk,pk):
        try:
            return SubCategory.objects.filter(category=catpk, category__dept=deptpk, category__dept__location=locpk, pk=pk)
        except SubCategory.DoesNotExist:
            raise Http404

    def get(self, request, locpk, deptpk, catpk,pk):
        locations = self.get_object(locpk, deptpk, catpk,pk)
        serializer = SubCategorySerializer(locations, many=True)
        return Response(serializer.data)

    def put(self, request, locpk, deptpk, catpk,pk):
        location = self.get_object(locpk, deptpk, catpk,pk).first()
        import pdb;pdb.set_trace()
        serializer = SubCategorySerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, locpk, deptpk,catpk,pk):
        location = self.get_object(locpk, deptpk, catpk,pk).first()
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SKUDataList(APIView):
    """
    List all SKUData, or create a new one
    """
    def get(self, request):
        skudata = SKUData.objects.all()
        serializer = SKUDataSerializer(skudata, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SKUDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SKUDataDetail(APIView):
    """
    Retrieve SKU info based on metadata.
    """

    def get_object(self, mtdata):
        try:
            data ={}
            mtdata = mtdata.split(",")
            if len(mtdata) == 4:
                data = SKUData.objects.filter(location__iexact=mtdata[0].strip(),department__iexact=mtdata[1].strip(),category__iexact=mtdata[2].strip(),subcategory__iexact=mtdata[3].strip())
            elif len(mtdata) == 3:
                data = SKUData.objects.filter(location__iexact=mtdata[0].strip(),department__iexact=mtdata[1].strip(),category__iexact=mtdata[2].strip())
            elif len(mtdata) == 2:
                data = SKUData.objects.filter(location__iexact=mtdata[0].strip(),department__iexact=mtdata[1].strip())
            elif len(mtdata) == 1:
                data = SKUData.objects.filter(location__iexact=mtdata[0].strip())
            return data
        except SKUData.DoesNotExist:
            raise Http404

    def get(self, request, mtdata):
        locations = self.get_object(mtdata)
        serializer = SKUDataSerializer(locations, many=True)
        return Response(serializer.data)
