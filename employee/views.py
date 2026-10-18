from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class EmployeeListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_object(self):
        return Employee.objects.get(user = self.request.user)

