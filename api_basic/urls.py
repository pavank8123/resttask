from django.urls import path
from api_basic import views

urlpatterns = [
    path('locations/', views.LocationList.as_view()),
    path('locations/<int:pk>/', views.LocationDetail.as_view()),
    path('locations/<int:pk1>/departments/', views.DepartmentList.as_view()),
    path('locations/<int:pk1>/departments/<int:pk>/', views.DepartmentDetail.as_view()),
    path('locations/<int:locpk>/departments/<int:deptpk>/categories/', views.CategoryList.as_view()),
    path('locations/<int:locpk>/departments/<int:deptpk>/categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('locations/<int:locpk>/departments/<int:deptpk>/categories/<int:catpk>/subcategories/', views.SubCategoryList.as_view()),
    path('locations/<int:locpk>/departments/<int:deptpk>/categories/<int:catpk>/subcategories/<int:pk>/', views.SubCategoryDetail.as_view()),
    path('skudata/', views.SKUDataList.as_view()),
    path('metadata/<str:mtdata>', views.SKUDataDetail.as_view()),
]

