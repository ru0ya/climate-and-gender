from django.db import models
from django.contrib.auth.models import User



class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    location = models.CharField(max_length=255)
    HEALTH_CONDITION_CHOICES = [
        ('asthmatic', 'Asthmatic'),
        ('pregnant', 'Pregnant'),
        ('other', 'Other'),
    ]
    health_condition = models.CharField(max_length=50, choices=HEALTH_CONDITION_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    next_of_kin = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
