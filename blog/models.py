from django.db import models
from users.models import CustomUser
# Create your models here.


class Odam(models.Model):
    object = None
    ism_famiya = models.CharField(max_length=200)
    mamlakati = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='rasm/', null=True, blank=True)
    uversitet = models.CharField(max_length=200)

    def __str__(self):
        return self.ism_famiya


class Ikon(models.Model):
    object = None
    text = models.TextField()
    ikon_rasm = models.ImageField(upload_to='ikon_rasm/', null=True, blank=True)

    def __str__(self):
        return self.text


class Sumpermision(models.Model):
    object = None
    text = models.TextField()
    name = models.CharField(max_length=100)
    narx = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Sponsr(models.Model):
    object = None
    name = models.CharField(max_length=100)
    sponsr_rasm = models.ImageField(upload_to='sponsr_rasm/', null=True, blank=True)

    def __str__(self):
        return self.name


class Maqola(models.Model):
    object = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    tel_raqam = models.IntegerField()
    affiliation = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    key_words = models.CharField(max_length=5)
    section = models.CharField(max_length=100)
    files = models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.first_name