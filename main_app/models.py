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
    state = models.CharField(max_length = 2)
    district = models.CharField(max_length = 150)
    address = models.CharField(max_length = 200)
    zipcode = models.IntegerField()
    grade = models.CharField(max_length = 1, choices=GRADES, default=GRADES[0][0],)
    teacher_name = models.CharField(max_length = 100, blank=True)
    teacher_email = models.EmailField(max_length = 100, blank=True)
    school_url = models.URLField(blank=True)
    notes = models.TextField(max_length = 250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher_name} at {self.school_name} with an id of {self.id}'

    def get_absolute_url(self):
        # return reverse('classroom_detail', kwargs={'classroom_id': self.id})      # use if classroom detail is view function
        return reverse('classroom_detail', kwargs={'pk': self.id})                  # use if classroom detail is CBV


class Item(models.Model):
    name = models.CharField(max_length = 100)
    amount = models.IntegerField(max_length = 50)
    thumbnail = models.URLField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    notes = models.TextField(max_length = 100, blank=True)

    def __str__(self):
        return self.item

    # def get_absolute_url(self):
    #     return reverse('item_detail', kwargs={'pk':self.id})