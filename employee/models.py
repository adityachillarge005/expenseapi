from django.db import models

from django.conf import settings
DEPT_CHOICES = [
    ('HR', 'Human Resources'),
    ('IT', 'Information Technology'),
    ('FIN', 'Finance'),
    ('MKT', 'Marketing'),
]
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="employee"
)
    emp_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    department = models.CharField(max_length=10,choices=DEPT_CHOICES)

    def __str__(self):
        return self.name