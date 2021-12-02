from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ' '+ self.name

class Department(models.Model):
    dep_name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' '+ self.dep_name


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    dept = models.ForeignKey(Department, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' '+ self.cat_name


class SubCategory(models.Model):
    sub_cat_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_cat_name

class SKUData(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)

    class Meta():
        index_together = [['subcategory', 'location', 'department', 'category']]
    def __str__(self):
        return self.name