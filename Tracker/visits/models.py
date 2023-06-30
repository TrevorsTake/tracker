from django.db import models
from django.contrib.auth.models import User

class Clinic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')  # Add the 'default' parameter here
    country = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # other fields ...

class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    notes = models.TextField()
    date = models.DateField()  # Make sure this field exists.
    # other fields ...


