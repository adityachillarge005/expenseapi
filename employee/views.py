from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class employees(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class employeeDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


