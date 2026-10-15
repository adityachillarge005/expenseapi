from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics
# Create your views here.

class employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class employeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


