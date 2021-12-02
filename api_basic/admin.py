from django.contrib import admin

# Register your models here.
from .models import Location, Department, Category, SubCategory, SKUData

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'dep_name', 'location')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name', 'dept', "location")

    def location(self,obj):
        return obj.dept.location.name


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_cat_name', 'category', "dept", "location")

    def dept(self, obj):
        return obj.category.dept

    def location(self, obj):
        return obj.category.dept.location.name


class SKUDatatAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'department', 'category', 'subcategory')


admin.site.register(SKUData,SKUDatatAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)