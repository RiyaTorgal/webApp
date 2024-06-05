from django.db import models

# Create your models here.
from django.db import models

class formdb(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    COUNTRY_CHOICES = [
        ('Europe', 'Europe'),
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('North America', 'North America'),
        ('South America', 'South America')
    ]

    fullName = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    country = models.CharField(max_length=15, choices=COUNTRY_CHOICES)
    phNo = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.fullName
