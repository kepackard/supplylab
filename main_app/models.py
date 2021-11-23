from django.db import models
from django.db.models.fields import IntegerField, URLField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

GRADES = (
    ('K', 'Kindergarten'),
    ('E', 'Elementary '),
    ('M', 'Middle School'),
    ('H', 'High School'),
)

class Classroom(models.Model):
    school_name = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    district = models.CharField(max_length = 150)
    address = models.CharField(max_length = 200)
    zipcode = models.IntegerField(max_length = 5)
    grade = models.CharField(max_length = 1, choices=GRADES, default=GRADES[0][0],)
    teacher_name = models.CharField(max_length = 100)
    teacher_email = models.EmailField(max_length = 100)
    school_url = models.URLField()
    notes = models.TextField(max_length = 250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher_name} at {self.school_name} with an id of {self.id}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'classroom_id': self.id})

    
