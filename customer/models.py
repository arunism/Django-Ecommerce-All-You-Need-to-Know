from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Not Specified', 'Not Specified'),
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    # username = models.CharField(max_length=20)
    # email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    country = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    street = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username
