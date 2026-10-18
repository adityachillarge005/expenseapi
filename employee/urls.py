from django.urls import path
from .import views
urlpatterns = [
    path('employees/',views.EmployeeListCreateView.as_view()),
    path('employeedetails/<int:pk>/',views.EmployeeRetrieveUpdateDestroyView.as_view()),
    path('employeeprofile/',views.EmployeeProfileView.as_view()),
]