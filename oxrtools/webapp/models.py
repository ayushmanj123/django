from django.db import models

# Create your models here.

class Aadhar_Front(models.Model):
    name = models.CharField(max_length=200, blank=False,  default="")
    aadhar_front = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name

class Aadhar_Back(models.Model):
    name = models.CharField(max_length=200, blank=False,  default="")
    aadhar_back = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name
