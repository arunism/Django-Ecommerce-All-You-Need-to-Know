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
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    country = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    street = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username

SERVICE_CHOICES = (
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Satisfactory','Satisfactory'),
    ('Bad','Bad')
)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='reviews')
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.user.username
