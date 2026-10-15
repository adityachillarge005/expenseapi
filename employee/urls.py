from django.urls import path
from .import views
urlpatterns = [
    path('employees/',views.employees.as_view()),
    path('employeedetails/<int:id>/',views.employeeDetails.as_view()),
]