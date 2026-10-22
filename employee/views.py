from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer , EmployeeProfileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.shortcuts import get_object_or_404
# Create your views here.

class EmployeeListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        dept = self.request.query_params.get("department")

        if dept:
            return Employee.objects.filter(department = dept)

        return Employee.objects.all()

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeProfileSerializer

    def get_object(self):
        return get_object_or_404(Employee,user = self.request.user)

