from django.db import models
from django.core.validators import MinLengthValidator

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=10,
                             validators=[MinLengthValidator(10)])
    course = models.CharField(max_length=100)\
    
    def __str__(self):
        return self.name
    