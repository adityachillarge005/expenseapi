from django.db import models
DEPT_CHOICES = [
    ('HR', 'Human Resources'),
    ('IT', 'Information Technology'),
    ('FIN', 'Finance'),
    ('MKT', 'Marketing'),
]
# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100,choices=DEPT_CHOICES)

    def __str__(self):
        return self.name