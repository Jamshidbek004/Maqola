from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Gender(models.Model):
    name = models.CharField(max_length=100)


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True )
    affliation = models.CharField(max_length=100)

    def __str__(self):
        return self.username

